from pydantic import BaseModel

from src.database.schemas import Usuario


class CriarTreino(BaseModel):
    pessoa: Usuario
    local_treino: str
    dias_max: int
    tempo_max_treino: int
