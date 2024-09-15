from pydantic import BaseModel

from src.database.schemas import Usuario


class CriarTreino(BaseModel):
    sexo: str
    idade: int
    peso: float
    altura: int
    local_treino: str
    tempo_max_treino: int
    dias_max: int
    tempo_total_treino: int