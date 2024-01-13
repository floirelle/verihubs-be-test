from .base import BaseException

class ForbiddenAccess(BaseException):
    def __init__(self, message="Forbidden access") -> None:
        super().__init__(403, message)