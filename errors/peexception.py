class PEException(Exception):
    def __init__(self, detail="") -> None:
        super().__init__(detail)