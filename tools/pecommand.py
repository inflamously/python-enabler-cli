# Equals to pecommand(args)(func). Also a curry function chaining.
import types
from typing import Any, Callable, Tuple, Union
from tools.peprinter import pe_print_error
from cmds.pesimpleerror import PECodeMessage
from errors.pesyntaxerror import PESyntaxError
from cmds.pesimpleerror import PE_SUCCESS
from cmds.peshell import runner
from os import environ


PEStringList = list[str]
PEList = Union[PEStringList, Tuple[Callable[[], Any], list[str], Callable[[], Any]]]
PECallable = Callable[..., PEList]
OptionalCallable = Union[Callable[[], Any], None]


class PECommand():
    def __init__(self, 
                commandlist: PEStringList,
                before_callback: OptionalCallable = None, 
                after_callback: OptionalCallable = None,
                desc: str = "",
                custom_env: dict[str, str] = {},
                shell=False) -> None:
        self.commandlist = commandlist
        self.before_callback = before_callback
        self.after_callback = after_callback
        self.desc = desc
        self.update_env(custom_env)
        self.shell=shell


    def validate(self) -> Tuple[bool, Any, int]:
        position: int = 1
        for value_index in range(len(self.commandlist)):
            if not isinstance(self.commandlist[value_index], str): return (False, self.commandlist[value_index], position)
            position += 1
        return (True, None, -1)
    
    
    def update_env(self, custom_env: Union[dict[str, str], None]=None):
        self.env = environ.copy()
        if custom_env:
            for key, value in custom_env.items():
                self.env.pop(key, None)
                self.env[key] = value
        print(self.env)


"""
Abstracts list of commands away to be executed by the runner line by line
"""
class PECommandDict():
    
    
    def __init__(self, *args: PECommand) -> None:
        self.commands = args
        

    def validate(self) -> Tuple[bool, Union[Any, None], Tuple[int, int]]:
        position = (1, 1);
        for pecommand in self.commands:
            if not isinstance(pecommand, PECommand): return (False, pecommand, position)
            value_valid, errored_value, position_index = pecommand.validate()
            position = (position[0] + 1, position_index)
            if not pecommand.validate: return (value_valid, errored_value, position)
        return (True, None, position)


    """
    Executes commands in commandlist and handles the error on the output of given command
    """
    def execute(self):
        for pecommand in self.commands:
            if pecommand.before_callback: pecommand.before_callback()
            pecodemessage = runner(pecommand.commandlist, desc=pecommand.desc, env=pecommand.env, shell=pecommand.shell)
            if isinstance(pecodemessage, PECodeMessage) and not pecodemessage == PE_SUCCESS:
                pe_print_error(pecommand.desc, pecodemessage.message, pecodemessage.data if hasattr(pecodemessage, 'data') else None)
            if pecommand.after_callback: pecommand.after_callback()


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