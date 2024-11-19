from sqlalchemy import insert, select, update, and_
from fastapi import UploadFile
from base64 import b64encode
from bcrypt import hashpw
from typing import Union, Dict
from uuid import uuid4
from os import environ

from src.database.usuario.tables import usuario_table
from src.database.utils import database
from src.database.usuario.schemas import (
    NovoUsuario, 
    UsuarioLogin, 
    Usuario,
    AtualizarInfo,
    AlterarFoto,
    AlterarSenha
)
from src.database.usuario.exception import (
    LoginFalha, 
    EmailJaUtilizado,
    TipoDeArquivoInvalido,
    SenhaIncorretaAlteracao
)


class UsuarioService:

    salt = environ.get("FIXED_SALT").encode()

    async def criar_usuario(self, dados: NovoUsuario) -> None:
        # Verificando se o email já está registrado
        select_query = select(usuario_table).where(usuario_table.email == dados.email)
        if await database.fetch_one(select_query) is not None:
            raise EmailJaUtilizado
        # Preparando query
        insert_query = insert(usuario_table).values(
            codigo = str(uuid4()),
            foto_perfil = self._enconde_bytes(self._busca_imagem_padrao()),
            nome = dados.nome,
            email = dados.email,
            senha = self._hash_senha(dados.senha)
        )
        # Inserindo no banco
        await database.execute(insert_query)

    async def login(self, data: UsuarioLogin) -> Usuario:
        result = await self._busca_usuario_senha(data.email, data.senha)
        if result is None:
            raise LoginFalha
        del result["senha"]
        return Usuario(**result)

    async def atualizar_infos(self, dados: AtualizarInfo) -> None:
        # Preparando query
        update_query = update(usuario_table).values(
            sexo = dados.sexo,
            idade = dados.idade,
            altura = dados.altura,
            total_meses_treino = dados.total_meses_treino
        ).where(usuario_table.codigo == str(dados.usuario))
        # Executando query
        await database.execute(update_query)

    async def alterar_senha(self, dados: AlterarSenha) -> None:
        # Verificando se a senha do usuário é a esperada
        if await self._busca_usuario_senha(dados.email, dados.senha_atual) is None:
            raise SenhaIncorretaAlteracao
        # Preparando query de update
        update_query = update(usuario_table).values(
            senha = self._hash_senha(dados.senha_nova)
        ).where(usuario_table.email == dados.email)
        # Realizando alteração de senha
        await database.execute(update_query)

    async def alterar_foto(self, dados: AlterarFoto) -> None:
        # Verificando se a imagem é válida
        nova_foto = await self._verifica_imagem(dados.foto_perfil)
        # Preparando query
        update_query = update(usuario_table).values(
            foto_perfil = nova_foto
        ).where(usuario_table.codigo == str(dados.usuario))
        # Executando query
        await database.execute(update_query)

    async def _busca_usuario_senha(self, email: str, senha: str) -> Union[Dict, None]:
        select_query = select(usuario_table).where(and_(
            usuario_table.email == email,
            usuario_table.senha == self._hash_senha(senha)
        ))
        return await database.fetch_one(select_query)
    
    async def _verifica_imagem(self, img: Union[UploadFile, None]) -> bytes:
        if img is None:
            return self._enconde_bytes(self._busca_imagem_padrao())
        elif img.content_type not in ["image/jpeg", "image/png"]:
            raise TipoDeArquivoInvalido
        return self._enconde_bytes(await img.read())

    def _hash_senha(self, password: str) -> bytes:
        return hashpw(password.encode(), self.salt)

    def _busca_imagem_padrao(self) -> bytes:
        with open("images/imagem-padrao-usuario.png", "rb") as f:
            return f.read()

    def _enconde_bytes(self, dados: bytes) -> bytes:
        return b64encode(dados)


usuario_service = UsuarioService()
