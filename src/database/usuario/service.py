from sqlalchemy import insert, select, and_
from bcrypt import gensalt, hashpw
from uuid import uuid4
from os import environ

from src.database.usuario.tables import usuario_table
from src.database.utils import database
from src.database.usuario.schemas import NovoUsuario, UsuarioLogin, Usuario
from src.database.usuario.exception import LoginFalha, EmailJaUtilizado


class UsuarioService:

    salt = environ.get("FIXED_SALT").encode()

    async def criar_usuario(self, dados: NovoUsuario) -> None:
        select_query = select(usuario_table).where(usuario_table.email == dados.email)
        if await database.fetch_one(select_query) is not None:
            raise EmailJaUtilizado
        insert_query = insert(usuario_table).values(
            codigo = str(uuid4()),
            nome = dados.nome,
            email = dados.email,
            senha = self.hash_senha(dados.senha),
            altura = dados.altura,
            total_meses_treino = dados.total_meses_treino
        )
        await database.execute(insert_query)

    async def login(self, data: UsuarioLogin) -> Usuario:
        select_query = select(usuario_table).where(and_(
            usuario_table.email == data.email,
            usuario_table.senha == self.hash_senha(data.senha)
            ))
        result = await database.fetch_one(select_query)
        if result is None:
            raise LoginFalha
        del result["senha"]
        return Usuario(**result)

    def hash_senha(self, password: str) -> bytes:
        return hashpw(password.encode(), self.salt)


usuario_service = UsuarioService()
