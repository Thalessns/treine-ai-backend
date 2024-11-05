from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

from src.llm.schemas import NewWorkout


class Workout(BaseModel):
    codigo: UUID
    user: UUID
    treino: NewWorkout
    data_criacao: datetime


class SaveNewWorkout(BaseModel):
    user: UUID
    workout: NewWorkout


class SelectUser(BaseModel):
    user: UUID