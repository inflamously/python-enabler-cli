from importlib.resources import files
from typing import Any
import toml


class AppConfig:
    def __init__(self) -> None:
        config_data = files("python_enabler").joinpath("main.toml").read_text()
        self.data = toml.loads(config_data)
        if "app" not in self.data:
            raise Exception("main.toml could not be loaded properly.")

    def __getitem__(self, key) -> Any:
        is_string = isinstance(key, str)
        is_dot_separated = True if is_string and len(key.split(".")) > 0 else False

        if is_string:
            if is_dot_separated:
                keys = key.split(".")
                result = None
                for found_key in keys:
                    result =  self.data[found_key] if not result else result[found_key]
                return result
            else:
                return self.data[key]
        else:
            return None
