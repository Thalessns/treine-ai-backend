from fastapi import APIRouter
from typing import List

from src.llm.client import client
from src.llm.schemas import CriarTreino, NovoTreino, Teste
from src.llm.constants import Prompts

from src.database.treino.service import treino_service
from src.database.treino.schemas import SalvarTreino, Treino

from src.database.usuario.service import usuario_service
from src.database.usuario.schemas import AtualizarInfo

treino_router = APIRouter(prefix="/treino")


@treino_router.post("/criar", status_code=201)
async def criar_treino(dados: CriarTreino) -> NovoTreino:
    gemini_resposta = None
    while gemini_resposta is None:
        gemini_resposta = await client.request_gemini_treino(dados, Prompts.CRIAR_TREINO)
    treino = NovoTreino(**gemini_resposta)
    await treino_service.criar_treino(SalvarTreino(
        usuario=dados.usuario,
        treino=treino
    ))
    await usuario_service.atualizar_infos(AtualizarInfo(**dados.model_dump()))
    return treino

@treino_router.post("/teste", status_code=201)
async def teste(dados: Teste):
    return await client.request_gemini(dados, Prompts.PROMPT_TESTE)

@treino_router.get("/selecionar-usuario", response_model=List[Treino])
async def selecionar_treinos_usuario(usuario: str) -> List[Treino]:
    return await treino_service.selecionar_treinos_usuario(usuario)
