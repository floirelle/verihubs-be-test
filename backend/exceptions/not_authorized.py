from .base import BaseException

class NotAuthorizedException(BaseException):
    def __init__(self, message="Not authorized error") -> None:
        super().__init__(401, message)