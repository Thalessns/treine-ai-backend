from fastapi import HTTPException


class DatabaseException(HTTPException):

    STATUS_CODE = -1
    DETAIL = ""

    def __init__(self):
        super().__init__(
            detail=self.DETAIL,
            status_code=self.STATUS_CODE
        )
