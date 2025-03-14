import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("I will execute steps in fixture method 1")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixture method 2")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixture method 3")