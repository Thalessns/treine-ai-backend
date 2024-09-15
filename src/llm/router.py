from fastapi import APIRouter, status

from src.llm.client import client
from src.llm.schemas import CriarTreino
from src.llm.constants import Prompts

llm_router = APIRouter(prefix="/llm")


@llm_router.post("/criar-treino", status_code=status.HTTP_201_CREATED)
async def submit(data: CriarTreino):
    return await client.request_gemini(data, Prompts.CRIAR_TREINO)