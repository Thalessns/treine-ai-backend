from fastapi import FastAPI

from src.llm.router import llm_router
from src.database.usuario.router import usuario_router
from src.database.treino.router import treino_router
from src.database.utils import Database

app = FastAPI(
    title="Treine.AI - API",
    version="1.0.0"
)

app.add_event_handler("startup", Database.init_models)
app.include_router(llm_router)
app.include_router(usuario_router)
app.include_router(treino_router)
