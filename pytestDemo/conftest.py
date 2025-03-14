import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("user details")
    return ["Stephin","Abraham","stephin123@gmail.com"]
