from fastapi import status

from src.database.exceptions import DatabaseException


class SenhasDiferentes(DatabaseException):

    STATUS_CODE = status.HTTP_406_NOT_ACCEPTABLE
    DETAIL = "As senhas estão diferentes."


class EmailJaUtilizado(DatabaseException):
    
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "O Email informado já foi utilizado"


class TipoDeArquivoInvalido(DatabaseException):

    STATUS_CODE = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    DETAIL = "A imagem deve ser jpeg ou png."


class LoginFalha(DatabaseException):

    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Erro no login, credenciais incorretas."


class SenhaIncorretaAlteracao(DatabaseException):
    
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Erro na alteração de senha, a senha atual está incorreta."