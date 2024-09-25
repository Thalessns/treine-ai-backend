from fastapi import status, HTTPException


class RequestException(HTTPException):

    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail: str):
        super().__init__(
            detail=detail,
            status_code=self.STATUS_CODE
        )


class ResponseException(HTTPException):

    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "Erro ao gerar novo treino. Por favor, tente novamente!"

    def __init__(self):
        super().__init__(
            detail=self.DETAIL,
            status_code=self.STATUS_CODE
        )
