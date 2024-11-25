from fastapi import status

from src.database.exceptions import DatabaseException


class UsuarioSemTreino(DatabaseException):

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Nenhum treino foi encontrado para o usuário especificado."


class TreinoNaoEncontrado(DatabaseException):

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "O código especificado não está vinculado a nenhum treino."
