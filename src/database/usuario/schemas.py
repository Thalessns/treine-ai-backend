from fastapi import UploadFile
from pydantic import BaseModel
from typing import Union
from uuid import UUID


class NovoUsuario(BaseModel):
    nome: str
    email: str
    senha: str


class UsuarioLogin(BaseModel):
    email: str
    senha: str


class Usuario(BaseModel):
    codigo: UUID
    foto_perfil: bytes
    nome: str
    email: str
    idade: Union[int, None]
    altura: Union[int, None]
    total_meses_treino: Union[int, None]


class AtualizarInfo(BaseModel):
    usuario: UUID
    sexo: str
    idade: int
    altura: int
    total_meses_treino: int


class AlterarSenha(BaseModel):
    email: str
    senha_atual: str
    senha_nova: str


class AlterarFoto(BaseModel):
    usuario: UUID
    foto_perfil: Union[UploadFile, None]
