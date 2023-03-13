from .peexception import PEException


class PEProjectException(PEException):
    def __init__(self, detail="") -> None:
        super().__init__(detail)


class PEProjectExceptionURLMismatch(PEProjectException):
    def __init__(self, detail="Given repository URL invalid") -> None:
        super().__init__(detail)
