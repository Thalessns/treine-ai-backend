from sqlalchemy import insert, select, and_
from bcrypt import gensalt, hashpw, checkpw
from uuid import uuid4

from src.database.user.tables import user
from src.database.utils import database
from src.database.user.schemas import NewUser, UserLogin, User
from src.database.user.exception import LoginFailure, EmailAlreadyUsed

class UserService:

    salt = gensalt()
    
    async def create_new_user(self, data: NewUser) -> None:
        select_query = select(user).where(user.email == data.email)
        if await database.fetch_one(select_query) is not None:
            raise EmailAlreadyUsed()
        insert_query = insert(user).values(
            codigo = uuid4(),
            nome = data.nome,
            email = data.email,
            senha = self.hash_password(data.senha),
            altura = data.altura,
            total_meses_treino = data.total_meses_treino
        )
        await database.execute(insert_query)

    async def login_user(self, data: UserLogin) -> User:
        select_query = select(user).where(and_(
            user.email == data.email,
            user.senha == self.hash_password(data.senha)
            ))
        result = await database.fetch_one(select_query)
        if result is None:
            raise LoginFailure
        del result["senha"]
        return User(**result)

    def hash_password(self, password: str) -> bytes:
        return hashpw(password.encode(), self.salt)

    def verify_password(self, stored_password: bytes, password: str) -> bool:
        return checkpw(password.encode(), stored_password)


user_service = UserService()
