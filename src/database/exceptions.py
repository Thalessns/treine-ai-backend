from fastapi import HTTPException
from fastapi import status

class DatabaseException(HTTPException):

    STATUS_CODE = -1
    DETAIL = ""

    def __init__(self):
        super().__init__(
            detail=self.DETAIL,
            status_code=self.STATUS_CODE
        )


class DatabaseEnvConfig(DatabaseException):

    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "Verifique a variável ENV no seu arquivo .env, ela deve ter o valor 'Server' ou 'Local'."