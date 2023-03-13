from typing import Union


def pe_print_command(desc: str, output: Union[str, None] = None):
    print('> ["{}"]'.format(desc.upper()))
    if output: print('{}'.format(output))