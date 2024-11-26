import json

from sqlalchemy import insert, select
from typing import List
from uuid import uuid4

from src.database.utils import database
from src.database.treino.schemas import Treino, SalvarTreino, ExerciciosAPI
from src.database.treino.tables import treino_table
from src.llm.schemas import NovoTreino
from src.database.treino.exceptions import UsuarioSemTreino, TreinoNaoEncontrado


class TreinoService:
    
    async def criar_treino(self, dados: SalvarTreino) -> SalvarTreino:
        dados.codigo = uuid4()
        insert_query = insert(treino_table).values(
            codigo = str(dados.codigo),
            usuario = str(dados.usuario),
            treino = dados.treino.model_dump_json()
        )
        await database.execute(insert_query)
        return dados

    async def selecionar_treinos_usuario(self, usuario: str) -> List[Treino]:
        select_query = select(treino_table).where(treino_table.usuario==usuario)
        treinos = await database.fetch_all(select_query)
        if treinos is None:
            raise UsuarioSemTreino
        result = list()
        for treino in treinos:
            treino["treino"] = NovoTreino(**json.loads(treino["treino"]))
            result.append(Treino(**treino))
        return result

    async def selecionar_treino(self, codigo: str) -> Treino:
        select_query = select(treino_table).where(treino_table.codigo == codigo)
        treino = await database.fetch_one(select_query)
        if treino is None:
            raise TreinoNaoEncontrado
        treino["treino"] = NovoTreino(**json.loads(treino["treino"]))
        return Treino(** treino)

    async def buscar_exercicios(self, codigo_treino: str) -> ExerciciosAPI:
        treino = await self.selecionar_treino(codigo_treino)
        dados = list()
        for dia in treino.treino.treino:
            for grupo, exercicios in dia.items():
                if grupo == "cardio": continue
                for ex, infos in exercicios.items():
                    ex_atual = list()
                    ex_atual.append(ex)
                    for value in infos.values(): ex_atual.append(value)
                    dados.append(ex_atual)
        return ExerciciosAPI(exercicios=dados)


treino_service = TreinoService()
