#Method name should have sense
#-k stands for method names execution, -s logs in out put -v stands for more info metadata
#you can run specific file with py.test <filename>
import pytest


@pytest.mark.smoke
def test_SecondProgram():
    msg = "Stephin Philip Abraham"
    assert msg == "Stephen Curry"

def test_Addition():
    a=5
    b=12
    assert a+7 == b , "The condition matches"