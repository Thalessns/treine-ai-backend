from fastapi import UploadFile
from pydantic import BaseModel
from typing import Union
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
    foto_perfil: bytes
    nome: str
    email: str
    altura: int
    total_meses_treino: int


class AlterarFoto(BaseModel):
    usuario: UUID
    foto_perfil: Union[UploadFile, None]
