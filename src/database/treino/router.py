from fastapi import APIRouter
from typing import List

from src.database.treino.schemas import Treino, SalvarTreino, SelecionarUsuario
from src.database.treino.service import treino_service

treino_router = APIRouter(prefix="/treino")


@treino_router.post("/criar", status_code=201)
async def criar_treino(dados: SalvarTreino) -> None:
    await treino_service.criar_treino(dados)


@treino_router.get("/selecionar-usuario", response_model=List[Treino])
async def selecionar_treinos_usuario(dados: SelecionarUsuario) -> List[Treino]:
    return await treino_service.selecionar_treinos_usuario(dados)
