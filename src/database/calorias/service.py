from sqlalchemy import insert, select, update
from typing import Union
from uuid import uuid4, UUID

from src.database.calorias.exceptions import PlanoCaloricoInexistente
from src.database.calorias.schemas import (
    CriarPlanoCalorico,
    PlanoCalorico, 
    SelecionarPlano
)
from src.database.calorias.tables import calorias_table
from src.database.utils import database


class CaloriasService:

    async def gerenciar_plano(self, dados: CriarPlanoCalorico) -> None:
        dados_db = await self._busca_plano(dados.usuario)
        if dados_db is None:
            await self._criar_plano(dados)
            return
        await self._atualizar_plano(dados, dados_db)

    async def selecionar_plano(self, dados: SelecionarPlano) -> PlanoCalorico:
        result = await self._busca_plano(dados.usuario)
        if result is None:
            raise PlanoCaloricoInexistente
        return result
    
    async def _criar_plano(self, dados: CriarPlanoCalorico) -> None:
        insert_query = insert(calorias_table).values(
            codigo = str(uuid4()),
            usuario = str(dados.usuario),
            carb_g = dados.carb_g,
            prot_g = dados.prot_g,
            gord_g = dados.gord_g,
            total_kcal = await self._calcula_total_calorias(dados)
        )
        await database.execute(insert_query)
    
    async def _atualizar_plano(self, dados_novos: CriarPlanoCalorico, dados_db: PlanoCalorico) -> None:
        temp_total = await self._calcula_total_calorias(dados_novos)
        update_query = update(calorias_table).values(
            carb_g = dados_novos.carb_g if dados_novos.carb_g != dados_db.carb_g else dados_db.carb_g,
            prot_g = dados_novos.prot_g if dados_novos.prot_g != dados_db.prot_g else dados_db.prot_g,
            gord_g = dados_novos.gord_g if dados_novos.gord_g != dados_db.gord_g else dados_db.gord_g,
            total_kcal = temp_total if temp_total != dados_db.total_kcal else dados_db.total_kcal
        ).where(calorias_table.usuario == str(dados_novos.usuario))
        await database.execute(update_query)

    async def _busca_plano(self, usuario: UUID) -> Union[PlanoCalorico, None]:
        select_query = select(calorias_table).where(calorias_table.usuario == str(usuario))
        result = await database.fetch_one(select_query)
        return PlanoCalorico(**result) if result is not None else None
    
    async def _calcula_total_calorias(self, dados: Union[CriarPlanoCalorico, PlanoCalorico]) -> int:
        return (4 * dados.carb_g) + (4 * dados.prot_g) + (9 * dados.gord_g)


calorias_service = CaloriasService()
