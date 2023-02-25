"""
Abstracts list of commands away to be executed by the runner line by line
"""


from typing import Any, Tuple, Union
from typing_extensions import Self
from cli.cmds.pecommand import OptionalCallable, PECommand
from cli.cmds.peshell import runner
from cli.errors.pesimpleerror import PE_SUCCESS, PECodeMessage


class PECommandDict:
    def __init__(self) -> None:
        self.commands: list[PECommand] = []

    def validate(self) -> Tuple[bool, Union[Any, None], Tuple[int, int]]:
        position = (1, 1)
        for pecommand in self.commands:
            if not isinstance(pecommand, PECommand):
                return (False, pecommand, position)
            value_valid, errored_value, position_index = pecommand.validate()
            position = (position[0] + 1, position_index)
            if not pecommand.validate:
                return (value_valid, errored_value, position)
        return (True, None, position)

    def new_command(
        self,
        commandlist: list[str],
        before_callback: OptionalCallable = None,
        after_callback: OptionalCallable = None,
        desc: str = "",
        custom_env: dict[str, str] = {},
        shell=False,
    ) -> Self:
        self.commands.append(
            PECommand(
                commandlist, before_callback, after_callback, desc, custom_env, shell
            )
        )
        return self

    """
    Executes commands in commandlist and handles the error on the output of given command
    """

    def execute(self) -> None:
        for pecommand in self.commands:
            if pecommand.before_callback:
                pecommand.before_callback()
            pecodemessage = runner(
                pecommand.construct_commands(),
                desc=pecommand.desc,
                env=pecommand.env,
                shell=pecommand.shell,
            )
            if (
                isinstance(pecodemessage, PECodeMessage)
                and not pecodemessage == PE_SUCCESS
            ):
                pecodemessage.exception(pecommand.desc, " ".join(pecommand.commandlist))
            if pecommand.after_callback:
                pecommand.after_callback()
