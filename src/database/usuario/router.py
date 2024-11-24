from fastapi import APIRouter

from src.database.usuario.schemas import (
    NovoUsuario, 
    UsuarioLogin, 
    Usuario,
    AlterarFoto,
    AlterarSenha
)
from src.database.usuario.service import usuario_service

usuario_router = APIRouter(prefix="/usuario")


@usuario_router.post("/criar", status_code=201)
async def criar(dados: NovoUsuario) -> str:
    await usuario_service.criar_usuario(dados)
    return "Usuário criado com sucesso!"


@usuario_router.get("/login", status_code=200)
async def login(email: str, senha: str) -> Usuario:
    return await usuario_service.login(UsuarioLogin(
        email=email,
        senha=senha
    ))


@usuario_router.put("/alterar-senha", status_code=201)
async def alterar_senha(dados: AlterarSenha) -> str:
    await usuario_service.alterar_senha(dados)
    return "Senha alterada com sucesso!"


@usuario_router.put("/alterar-foto", status_code=201)
async def alterar_foto(dados: AlterarFoto) -> str:
    await usuario_service.alterar_foto(dados)
    return "Foto alterada com sucesso!"
