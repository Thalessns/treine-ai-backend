import json

from sqlalchemy import insert, select
from typing import List
from uuid import UUID, uuid4

from src.database.utils import database
from src.database.workout.schemas import Workout, SaveNewWorkout, SelectUser
from src.database.workout.tables import workout
from src.llm.schemas import NewWorkout
from src.database.workout.exceptions import UserWorkoutsNotFound


class WorkoutService:
    
    async def create_new_workout(self, data: SaveNewWorkout) -> None:
        insert_query = insert(workout).values(
            codigo = uuid4(),
            user = data.user,
            treino = data.workout.model_dump_json()
        )
        await database.execute(insert_query)

    async def select_user_workouts(self, data: SelectUser) -> List[Workout]:
        select_query = select(workout).where(workout.user==data.user)
        workouts = await database.fetch_all(select_query)
        if workouts is None:
            raise UserWorkoutsNotFound
        result = list()
        for workout_dict in workouts:
            workout_dict["treino"] = NewWorkout(**json.loads(workout_dict["treino"]))
            result.append(Workout(**workout_dict))
        return result


workout_service = WorkoutService()
