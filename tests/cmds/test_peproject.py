import os
from tempfile import TemporaryDirectory

from python_enabler.cmds.peproject import install


def test_permission_tempdir():
    with TemporaryDirectory() as tempdirectory:
        print("created temporary directory", tempdirectory)
        assert os.path.exists(tempdirectory) == True


def test_project_install(mocker):
    mocker.patch("python_enabler.cmds.pecommanddict.PECommandDict.execute")
    with TemporaryDirectory() as tempdirectory:
        install(
            "git@github.com:inflamously/python-enabler-.git",
            tempdirectory,
            "test_token_whatever",
        )
        assert os.path.exists(tempdirectory) == True
