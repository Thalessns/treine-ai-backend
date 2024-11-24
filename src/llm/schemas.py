from pydantic import BaseModel
from typing import Dict, Any
from uuid import UUID

class CriarTreino(BaseModel):
    usuario: UUID
    objetivo: str
    sexo: str
    idade: int
    peso: float
    altura: int
    local_treino: str
    horas_max_treino: int
    dias_max_treino: int
    total_meses_treino: int


class NovoTreino(BaseModel):
    objetivo: str
    treino: Dict[str, Any]

