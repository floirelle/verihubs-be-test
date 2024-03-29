from fastapi import HTTPException

class BaseException(Exception):
    def __init__(self, status_code, message) -> None:
        self.status_code = status_code
        self.message = message