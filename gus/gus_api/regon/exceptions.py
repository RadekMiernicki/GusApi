from typing import Optional

class ResponseException(Exception):
    """
    General response exception
    """
    pass

class EmptyResponse(ResponseException):
    """
    Empty response
    """
    pass

class UnexpectedResponse(ResponseException):
    """
    Unexpected response
    """
    pass

class RegonAPIError(ResponseException):

    def __init__(self, message:str, code:Optional[int]):
        self.message = str(message)
        try:
            self.code = int(code)
        except (TypeError, ValueError):
            self.code = None

    def __str__(self):
        return self.message