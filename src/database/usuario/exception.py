from fastapi import status

from src.database.exceptions import DatabaseException


class EmailJaUtilizado(DatabaseException):
    
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "O Email informado já foi utilizado"


class LoginFalha(DatabaseException):

    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Erro no login, credenciais incorretas."
