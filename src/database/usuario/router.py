from fastapi import APIRouter

from src.database.usuario.schemas import (
    NovoUsuario, 
    UsuarioLogin, 
    Usuario,
    AlterarFoto
)
from src.database.usuario.service import usuario_service

usuario_router = APIRouter(prefix="/usuario")


@usuario_router.post("/criar", status_code=201)
async def criar(dados: NovoUsuario) -> None:
    await usuario_service.criar_usuario(dados)


@usuario_router.get("/login", status_code=200)
async def login(dados: UsuarioLogin) -> Usuario:
    return await usuario_service.login(dados)


@usuario_router.put("/alterar-foto", status_code=201)
async def alterar_foto(dados: AlterarFoto) -> None:
    await usuario_service.alterar_foto(dados)
