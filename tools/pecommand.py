# Equals to pecommand(args)(func). Also a curry function chaining.
from typing import Any, Callable, Tuple, Union
from cli.cmds.pesimpleerror import PE_ERROR_GENERIC
from cmds.peshell import runner


"""
Abstracts list of commands away to be executed by the runner line by line
"""
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

    """
    Executes commands in commandlist and handles the error on the output of given command
    """
    def execute(self):
        for key, command in self.commandlist.items():
            pecodemessage = runner(command, desc=key)
            # TODO: Implement check if we are given an error. 
            if pecodemessage.has_error():
                ...


"""
(@pecommand(<xyz>))(func)
"""
# TODO: Check if this decorator should instead pass commands in a dict and not the target function?
def pecommand(commandlist: PECommandDict):
    def inner(original_func: Callable):
        # Evaluate function
        valid_syntax, data, index = commandlist.validate()
        
        # Raise error if parsing failed
        if not valid_syntax: raise PESyntaxError(index, data)
        
        # Return a modified func version where commandlist gets called at the end
        def modified_func():
            original_func()
            commandlist.execute()
        
        modified_func.__name__ = original_func.__name__
        
        # Return if parsing passed
        return modified_func
    return inner