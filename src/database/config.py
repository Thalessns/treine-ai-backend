from dotenv import load_dotenv
from os import environ

from src.database.exceptions import DatabaseEnvConfig

load_dotenv()


class DBConfigLocal():
    conn_url = f"sqlite+aiosqlite:///src/database/sqlite_db.db"


class DBConfigServer():
    conn_url = f"mysql+aiomysql://{environ.get('MYSQL_USER')}:{environ.get('MYSQL_PASSWORD')}@/treine_ai"


db_config = object

if environ.get("DB_TYPE") == "Server":
    db_config = DBConfigServer()
elif environ.get("DB_TYPE") == "Local":
    db_config = DBConfigLocal()
else:
    raise DatabaseEnvConfig
