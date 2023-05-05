from fastapi import HTTPException


class APIException(HTTPException):
    def __init__(self, detail: str, status_code: int):
        self.detail = detail
        self.status_code = status_code
        super().__init__(status_code, detail)
