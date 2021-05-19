import pytest

from vending_machine.drink import Cola
from vending_machine.drink_box import DrinkBox


class TestInfo:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.drink_box = DrinkBox()

    def test_normal(self):
        actual = self.drink_box.info()
        expected = [
            {
                "drink": Cola,
                "amount": 5,
            }
        ]
        assert actual == expected
