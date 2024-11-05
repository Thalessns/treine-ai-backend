from sqlalchemy import (Column, UUID, JSON, DateTime, ForeignKey, func)
from datetime import datetime

from src.database.utils import Base


class Workout(Base):
    __tablename__ = "Workout"

    codigo = Column(UUID, primary_key=True)
    user = Column(UUID, ForeignKey("User.codigo"), nullable=False)
    treino = Column(JSON, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now())
    

workout = Workout
