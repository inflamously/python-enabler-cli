"""
This ensures that the passed function name does not break due to changes to the function.
"""


from python_enabler.cmds.pecommanddict import PECommandDict


def test_pecommanddict_command_creation() -> None:
    commanddict: PECommandDict = PECommandDict().new_command(
        ["git", "clone", "target"], desc="Clones a target"
    )
    assert len(commanddict.commands) == 1
    assert commanddict.commands[0].commandlist == ["git", "clone", "target"]
    assert commanddict.commands[0].construct_commands() == "git clone target"
