from pydantic import BaseModel
from uuid import UUID


class NovoUsuario(BaseModel):
    nome: str
    email: str
    senha: str
    idade: int
    altura: int
    total_meses_treino: int


class UsuarioLogin(BaseModel):
    email: str
    senha: str


class Usuario(BaseModel):
    codigo: UUID
    nome: str
    email: str
    altura: int
    total_meses_treino: int
