from fastapi import APIRouter
from typing import List
from uuid import UUID

from src.database.workout.schemas import Workout, SaveNewWorkout, SelectUser
from src.database.workout.service import workout_service

workout_router = APIRouter(prefix="/database/workout")


@workout_router.post("/create", status_code=201)
async def create_workout(data: SaveNewWorkout) -> None:
    await workout_service.create_new_workout(data)


@workout_router.get("/select-user", response_model=List[Workout])
async def select_user_workouts(data: SelectUser) -> List[Workout]:
    return await workout_service.select_user_workouts(data)
