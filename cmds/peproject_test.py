import os
from tempfile import TemporaryDirectory
import pytest
from cli.cmds.peproject import install


def test_permission_tempdir():
    with TemporaryDirectory() as tempdirectory:
        print('created temporary directory', tempdirectory)
        assert os.path.exists(tempdirectory) == True



def test_project_install():
    with TemporaryDirectory() as tempdirectory:
        install("git@github.com:inflamously/python-enabler-cli.git", tempdirectory, "test_token_whatever")
        assert os.path.exists(tempdirectory) == True