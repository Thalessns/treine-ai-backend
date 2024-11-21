from fastapi import APIRouter
from typing import List

from src.llm.client import client
from src.llm.schemas import CriarTreino, NovoTreino
from src.llm.constants import Prompts

from src.database.treino.service import treino_service
from src.database.treino.schemas import SalvarTreino, Treino, SelecionarUsuario

from src.database.usuario.service import usuario_service
from src.database.usuario.schemas import AtualizarInfo

treino_router = APIRouter(prefix="/treino")


@treino_router.post("/criar", status_code=201)
async def criar_treino(dados: CriarTreino) -> NovoTreino:
    treino = NovoTreino(** await client.request_gemini(dados, Prompts.CRIAR_TREINO))
    await treino_service.criar_treino(SalvarTreino(
        usuario=dados.usuario,
        treino=treino
    ))
    await usuario_service.atualizar_infos(AtualizarInfo(**dados.model_dump()))
    return treino



@treino_router.get("/selecionar-usuario", response_model=List[Treino])
async def selecionar_treinos_usuario(dados: SelecionarUsuario) -> List[Treino]:
    return await treino_service.selecionar_treinos_usuario(dados)
