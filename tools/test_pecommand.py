from cli.tools.pecommand import PECommandDict, pecommand

"""
This ensures that the passed function name does not break due to changes to the function.
"""
def test_pecommand_original_function_name():
    empty_commandlist = PECommandDict({})
    def custom_function(): ...
    assert pecommand(empty_commandlist)(custom_function).__name__ == "custom_function"