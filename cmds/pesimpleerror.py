from itertools import count
from typing import Union

class PECodeMessage():

    def __init__(self, code: Union[int, None] = 0x0, message: str = "") -> None:
        self.code = code
        self.message = message
        

    def __call__(self, custom_code: int):
        self.code = custom_code
        return self
    
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, PECodeMessage):
            return self.code == __o.code
        else:
            return False
    

    def value(self):
        return [self.code, self.message]