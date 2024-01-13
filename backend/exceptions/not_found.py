from .base import BaseException

class NotFoundException(BaseException):
    def __init__(self, message="Resource not found") -> None:
        super().__init__(404, message)