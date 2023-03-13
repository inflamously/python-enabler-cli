from .errors.peexception import PEException

class PESyntaxError(PEException):
    def __init__(self, position, data, detail="Invalid syntax") -> None:
        super().__init__(detail + " at line {}:{} => [{}]".format(position[0], position[1], data))