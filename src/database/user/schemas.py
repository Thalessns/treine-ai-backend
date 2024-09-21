from pydantic import BaseModel
from uuid import UUID

class NewUser(BaseModel):
    nome: str
    email: str
    senha: str
    idade: int
    altura: int
    total_meses_treino: int


class UserLogin(BaseModel):
    email: str
    senha: str


class User(BaseModel):
    codigo: UUID
    nome: str
    email: str
    altura: int
    total_meses_treino: int