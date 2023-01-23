from typing import Any, Union


PE_NONE = (1 << 0)


class PECodeMessage():
    
    
    value: int
    data: Any
    message: str
    

    def __init__(self, value: int = PE_NONE, message: str = "") -> None:
        self.value = value
        self.message = message


    def __call__(self, custom_code: Union[int, None] = None, message: Union[str, None] = None):
        self.value = custom_code if custom_code else self.value
        self.message = message if message else self.message
        return self
    
    
    def assign_data(self, data: Any):
        self.data = data
        return self
    

    def __repr__(self) -> str:
        return str(self.value)
    

    def __eq__(self, __x: object) -> bool:
        if isinstance(__x, PECodeMessage):
            return (self.value & __x.value) == __x.value
        elif isinstance(__x, int):
            return (self.value & __x) == __x
        else:
            return False


PE_SUCCESS = PECodeMessage((PE_NONE << 1), "Success") # Always ...xxx01
PE_ERROR_GENERIC = PECodeMessage((PE_NONE << 2), "Error occured") # Always ...xxx10
PE_ERROR_PLATFORM = PECodeMessage((PE_NONE << 3), "Platform not supported")
PE_ERROR_FILENOTFOUND = PECodeMessage((PE_NONE << 4), message="OS File not found")
PE_ERROR_COMMAND = PECodeMessage((PE_NONE << 5))


if not (PE_NONE == (1 << 0)): raise Exception("PE_NONE is empty and must be 0001")
if not (PE_SUCCESS == (PE_NONE << 1)): raise Exception("PE_SUCCESS must be 0010")
if not (PE_ERROR_GENERIC == (PE_NONE << 2)): raise Exception("PE_ERROR_GENERIC must be 0100")