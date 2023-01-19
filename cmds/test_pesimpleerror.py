from cli.cmds.pesimpleerror import PECodeMessage


def test_multiple_error_counter():
    A = PECodeMessage()
    assert A.code == 0x0
    B = PECodeMessage(0xCE0001)
    assert B.code == 0xCE0001
    C = PECodeMessage(0xCE0002)
    assert C.code == 0xCE0002
    

def test_custom_code_support():
    A = PECodeMessage()
    A(0xCE0666)
    assert A.code == 0xCE0666
    

def test_error_message():
    A = PECodeMessage(message="Hello World!")
    assert A.message == "Hello World!"
    

def test_error_code_eq_check():
    A = PECodeMessage(0xCE0666)
    assert A.code == 0xCE0666
    B = PECodeMessage(0xCE0667)
    assert B.code == 0xCE0667
    assert not (A == B)