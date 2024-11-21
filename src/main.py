from fastapi import FastAPI

from src.database.usuario.router import usuario_router
from src.database.treino.router import treino_router
from src.database.calorias.router import calorias_router
from src.database.utils import Database

app = FastAPI(
    title="Treine.AI - API",
    version="1.0.0"
)

app.add_event_handler("startup", Database.init_models)
app.include_router(usuario_router)
app.include_router(treino_router)
app.include_router(calorias_router)
