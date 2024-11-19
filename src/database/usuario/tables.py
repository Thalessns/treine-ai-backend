from sqlalchemy import (Column, String, Integer, BLOB, LargeBinary)

from src.database.utils import Base


class UsuarioTable(Base):
    __tablename__ = "usuario"
    
    codigo = Column(String(length=255), primary_key=True)
    foto_perfil = Column(LargeBinary, nullable=False)
    nome = Column(String(length=100), nullable=False)
    sexo = Column(String(length=20), nullable=True)
    email = Column(String(length=50), nullable=False)
    senha = Column(BLOB, nullable=False)
    idade = Column(Integer, nullable=True)
    altura = Column(Integer, nullable=True)
    total_meses_treino = Column(Integer, nullable=True)


usuario_table = UsuarioTable
