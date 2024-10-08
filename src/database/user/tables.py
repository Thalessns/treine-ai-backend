from sqlalchemy import (Column, String, Integer, UUID, BLOB)

from src.database.utils import Base


class User(Base):
    __tablename__ = "User"
    
    codigo = Column(UUID, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(BLOB, nullable=False)
    altura = Column(Integer, nullable=False)
    total_meses_treino = Column(Integer, nullable=False)


user = User
