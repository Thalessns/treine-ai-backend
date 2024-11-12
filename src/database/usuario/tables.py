from sqlalchemy import (Column, String, Integer, BLOB, LargeBinary)

from src.database.utils import Base


class UsuarioTable(Base):
    __tablename__ = "usuario"
    
    codigo = Column(String(length=255), primary_key=True)
    foto_perfil = Column(LargeBinary, nullable=False)
    nome = Column(String(length=100), nullable=False)
    email = Column(String(length=50), nullable=False)
    senha = Column(BLOB, nullable=False)
    altura = Column(Integer, nullable=False)
    total_meses_treino = Column(Integer, nullable=False)


usuario_table = UsuarioTable
