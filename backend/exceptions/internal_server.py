from .base import BaseException

class InternalServerException(BaseException):
    def __init__(self, message="Internal server error") -> None:
        super().__init__(500, message)