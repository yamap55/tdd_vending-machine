from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Bill1000, Coin10, Coin50, Coin100
import pytest


class TestInsert:
    @pytest.mark.parametrize("coin", [Coin10(), Coin50(), Coin100(), Bill1000()])
    def test_insert_coin(self, coin):
        try:
            VendingMachine().insert(coin)
        except Exception as e:
            pytest.fail(e)
