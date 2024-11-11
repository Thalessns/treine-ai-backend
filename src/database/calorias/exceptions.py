from fastapi import status

from src.database.exceptions import DatabaseException


class PlanoCaloricoInexistente(DatabaseException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "O usuário especificado ainda não possui um plano alimentar"
