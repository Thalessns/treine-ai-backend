from fastapi import status

from src.database.exceptions import DatabaseException


class UserWorkoutsNotFound(DatabaseException):

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Nenhum treino foi encontrado para o usuário especificado."
