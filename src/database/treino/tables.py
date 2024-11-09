from sqlalchemy import (Column, UUID, JSON, DateTime, ForeignKey)
from datetime import datetime

from src.database.utils import Base


class TreinoTable(Base):
    __tablename__ = "treino"

    codigo = Column(UUID, primary_key=True)
    usuario = Column(UUID, ForeignKey("usuario.codigo"), nullable=False)
    treino = Column(JSON, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now())
    

treino_table = TreinoTable
