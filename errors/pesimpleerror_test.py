
from cli.errors.pesimpleerror import PE_NONE, PE_SUCCESS, PECodeMessage


def test_multiple_error_counter():
    A = PECodeMessage()
    assert A == PE_NONE
    B = PECodeMessage(0x0001)
    assert B == 0x0001
    

def test_custom_code_support():
    A = PECodeMessage()
    A(0xCE0666)
    assert A == 0xCE0666
    

def test_error_message():
    A = PECodeMessage(message="Hello World!")
    assert A.message == "Hello World!"
    

def test_error_code_eq_check():
    A = PECodeMessage(0xCE0666)
    assert A == 0xCE0666
    B = PECodeMessage(0xCE0667)
    assert B == 0xCE0667
    assert not (A == B)
    
    
def test_equals_check():
    A = PECodeMessage(0x0001)
    B = PECodeMessage(0x0001)
    assert A == 0x0001
    assert B == 0x0001
    assert A == B
    

def test_repr_check():
    A = PECodeMessage(0x0001)
    assert str(A) == "1"
    

"""
Make sure we fixed PE_SUCCESS so we avoid issues later on.
"""
def test_code_check():
    assert PE_SUCCESS == int("0010", 2)