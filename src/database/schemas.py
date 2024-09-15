from pydantic import BaseModel


class Usuario(BaseModel):
    codigo: int
    nome: str
    idade: int
    altura: int
    tempo_total_treino: int
    