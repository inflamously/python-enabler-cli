from typing import Any, Callable, Tuple, Union
from os import environ


PEList = Union[list[str], Tuple[Callable[[], Any], list[str], Callable[[], Any]]]
PECallable = Callable[..., PEList]
OptionalCallable = Union[Callable[[], Any], None]


class PECommand:
    def __init__(
        self,
        commandlist: list[str],
        before_callback: OptionalCallable = None,
        after_callback: OptionalCallable = None,
        desc: str = "",
        custom_env: dict[str, str] = {},
        shell=False,
    ) -> None:
        self._commandlist: list[str] = commandlist
        self.before_callback = before_callback
        self.after_callback = after_callback
        self.desc: str = desc
        self.update_env(custom_env)
        self.shell: bool = shell

    def validate(self) -> Tuple[bool, Any, int]:
        position: int = 1
        for value_index in range(len(self._commandlist)):
            if not isinstance(self._commandlist[value_index], str):
                return (False, self._commandlist[value_index], position)
            position += 1
        return (True, None, -1)

    def update_env(self, custom_env: Union[dict[str, str], None] = None) -> None:
        self.env: dict[str, str] = environ.copy()
        if custom_env:
            for key, value in custom_env.items():
                self.env.pop(key, None)
                self.env[key] = value

    @property
    def commandlist(self):
        return self._commandlist

    def construct_commands(self) -> str:
        return " ".join(self._commandlist)
