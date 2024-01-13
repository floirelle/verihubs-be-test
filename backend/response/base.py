class BaseResponse():
    def __init__(self,status_code,message,data=None) -> None:
        self.status_code = status_code
        self.message = message
        self.data = data