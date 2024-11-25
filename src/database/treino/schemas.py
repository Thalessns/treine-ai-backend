from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

from src.llm.schemas import NovoTreino


class Treino(BaseModel):
    codigo: UUID
    usuario: UUID
    treino: NovoTreino
    data_criacao: datetime


class SalvarTreino(BaseModel):
    usuario: UUID
    codigo: Optional[UUID] = None
    treino: NovoTreino


class SelecionarUsuario(BaseModel):
    usuario: UUID
