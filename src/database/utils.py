from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy import MetaData
from typing import Union, List, Dict

from src.database.config import db_config

Base = declarative_base(metadata=MetaData())
engine = create_async_engine(url=db_config.conn_url)


class Database():

    async def fetch_all(self, query) -> Union[List[Dict], None]:
        cursor = await self.execute(query)
        rows = cursor.fetchall()
        if len(rows) < 1:
            return None
        return self.parse_content([row._mapping for row in rows])

    async def fetch_one(self, query) -> Union[Dict, None]:
        cursor = await self.execute(query)
        res = cursor.fetchone()
        if res is None:
            return None
        return self.parse_content(res._mapping)

    async def execute(self, query): 
        async with engine.begin() as conn:
            return await conn.execute(query)

    def parse_content(self, content: Union[Dict, List[Dict]]) -> Union [Dict, List[Dict]]:
        if type(content) is list:
            result = []
            for row in content:
                data = {}
                for key in row.keys():
                    data[key] = row[key]
                result.append(data)
            return result
        result = {}
        for key in content.keys():
            result[key] = content[key]
        return result

    @staticmethod
    async def init_models() -> None:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


database = Database()