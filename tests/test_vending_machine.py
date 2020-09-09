from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Bill1000, Coin10, Coin50, Coin100
import pytest


class TestInsert:
    @pytest.mark.parametrize("money", [Coin10(), Coin50(), Coin100(), Bill1000()])
    def test_insert_money(self, money):
        try:
            VendingMachine().insert(money)
        except Exception as e:
            pytest.fail(e)

    def test_insert_multiple_money(self):
        try:
            VendingMachine().insert(Coin10(), Coin50())
        except Exception as e:
            pytest.fail(e)
