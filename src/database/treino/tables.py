from sqlalchemy import (Column, String, JSON, DateTime, ForeignKey)
from datetime import datetime

from src.database.utils import Base


class TreinoTable(Base):
    __tablename__ = "treino"

    codigo = Column(String(length=255), primary_key=True)
    usuario = Column(String(length=255), ForeignKey("usuario.codigo"), nullable=False)
    treino = Column(JSON, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now())
    

treino_table = TreinoTable
