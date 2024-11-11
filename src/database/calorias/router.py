from fastapi import APIRouter

from src.database.calorias.schemas import (
    CriarPlanoCalorico,
    PlanoCalorico,
    SelecionarPlano
)
from src.database.calorias.service import calorias_service

calorias_router = APIRouter(prefix="/calorias")


@calorias_router.post("/criar", status_code=201)
async def criar_plano(dados: CriarPlanoCalorico) -> None:
    await calorias_service.gerenciar_plano(dados)


@calorias_router.get("/selecionar-plano", response_model=PlanoCalorico)
async def selecionar_plano(dados: SelecionarPlano) -> PlanoCalorico:
    return await calorias_service.selecionar_plano(dados)
