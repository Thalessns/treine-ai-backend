from pydantic import BaseModel


class Usuario(BaseModel):
    codigo: int
    nome: str
    idade: int
    altura: float
    tempo_total_treino: int
    