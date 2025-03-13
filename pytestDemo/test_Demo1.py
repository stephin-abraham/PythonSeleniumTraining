# any pytest file should begin with test_ or end with _test
#pytest method names should begin with test
# any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_FirstProgram():
    print("Hello This is the First Pytest program")
@pytest.mark.skip
def test_greet():
    print("Good morning all")
