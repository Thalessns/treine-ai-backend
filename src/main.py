from fastapi import FastAPI

from src.llm.router import llm_router
from src.database.user.router import user_router
from src.database.utils import Database

app = FastAPI(
    title="Treine.AI - API",
    version="0.1.0"
)

app.add_event_handler("startup", Database.init_models)
app.include_router(llm_router)
app.include_router(user_router)
