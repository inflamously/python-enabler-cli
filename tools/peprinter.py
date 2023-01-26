from typing import Any, Union


def pe_print_error(desc: str, message: Union[str, None] = None, data: Union[Any, None] = None):
    print('> ["ERROR" -> "{}:{}"]'.format(desc, data if data else None))
    if message: print('{}'.format(message))


def pe_print_command(desc: str, output: Union[str, None] = None):
    print('> ["{}"]'.format(desc.upper()))
    if output: print('{}'.format(output))