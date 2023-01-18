# Equals to pecommand(args)(func). Also a curry function chaining.
from typing import Any, Callable, Tuple, Union
from cmds.peshell import runner
from errors.pesyntaxerror import PESyntaxError

class PECommandDict():
    def __init__(self, commandlist: dict[str, list[str]]) -> None:
        self.commandlist = commandlist
        
    def validate(self) -> Tuple[bool, Union[Any, None], Tuple[int, int]]:
        position = (1, 1);
        for key, value in self.commandlist.items():
            if not isinstance(key, str): return (False, key, position)
            if not isinstance(value, list): return (False, value, position)
            if len(value) <= 0: return (False, value, position)
            for value_index in range(len(value)):
                if not isinstance(value[value_index], str): return (False, value[value_index], position)
                position = (position[0], position[1] + 1)
            position = (position[0] + 1, position[1])
        return (True, None, position)


    def execute(self):
        for key, command in self.commandlist.items():
            runner(command, desc=key)


"""
(@pecommand(<xyz>))(func)
"""
# TODO: Check if this decorator should instead pass commands in a dict and not the target function?
def pecommand():
    def inner(func: Callable[..., PECommandDict]):
        commandlist = func()
        
        # Evaluate function
        valid_syntax, data, index = commandlist.validate()
        
        # Raise error if parsing failed
        if not valid_syntax: raise PESyntaxError(index, data)
        
        # Run commands
        commandlist.execute()
        
        # Return if parsing passed
        return func
    return inner