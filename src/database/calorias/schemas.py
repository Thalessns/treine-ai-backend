from pydantic import BaseModel
from uuid import UUID


class CriarPlanoCalorico(BaseModel):
    usuario: UUID
    carb_g: int
    prot_g: int
    gord_g: int


class PlanoCalorico(BaseModel):
    codigo: str
    usuario: str
    carb_g: int
    prot_g: int
    gord_g: int
    total_kcal: int


class SelecionarPlano(BaseModel):
    usuario: UUID
