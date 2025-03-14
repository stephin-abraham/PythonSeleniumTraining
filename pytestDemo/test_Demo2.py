#Method name should have sense
#-k stands for method names execution, -s logs in out put -v stands for more info metadata
#you can run specific file with py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases conftest file to
import pytest


@pytest.mark.smoke
def test_SecondProgram():
    msg = "Stephin Philip Abraham"
    assert msg == "Stephen Curry"

def test_Addition():
    a=5
    b=12
    assert a+7 == b , "The condition matches"