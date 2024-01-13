from .base import BaseException

class BadRequestException(BaseException):
    def __init__(self, message="Bad request error") -> None:
        super().__init__(400, message)