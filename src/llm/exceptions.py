from fastapi import status, HTTPException


class RequestException(HTTPException):

    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail: str):
        super().__init__(
            detail=detail,
            status_code=self.STATUS_CODE
        )
