from fastapi import APIRouter, status

from src.llm.client import client
from src.llm.schemas import CriarTreino, NovoTreino
from src.llm.constants import Prompts

from src.database.treino.service import treino_service
from src.database.treino.schemas import SalvarTreino

from src.database.usuario.service import usuario_service
from src.database.usuario.schemas import AtualizarInfo

llm_router = APIRouter(prefix="/llm")


@llm_router.post("/criar-treino", status_code=status.HTTP_201_CREATED)
async def criar_treino(dados: CriarTreino) -> NovoTreino:
    treino = NovoTreino(** await client.request_gemini(dados, Prompts.CRIAR_TREINO))
    await treino_service.criar_treino(SalvarTreino(
        usuario=dados.usuario,
        treino=treino
    ))
    await usuario_service.atualizar_infos(AtualizarInfo(**dados.model_dump()))
    return treino
