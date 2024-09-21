from pydantic import BaseModel

class CriarTreino(BaseModel):
    sexo: str
    idade: int
    peso: float
    altura: int
    local_treino: str
    horas_max_treino: int
    dias_max_treino: int
    total_meses_treino: int