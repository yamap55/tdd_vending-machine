from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Coin10Yen, Coin50Yen, Coin100Yen, Coin500Yen, Bill1000Yen
import pytest


class TestVendingMachine:
    def setup_method(self, method):
        self.vending_machine = VendingMachine()

    @pytest.mark.parametrize(
        "money, amount",
        [
            (Coin10Yen(), 10),
            (Coin50Yen(), 50),
            (Coin100Yen(), 100),
            (Coin500Yen(), 500),
            (Bill1000Yen(), 1000),
        ],
    )
    def test_insert(self, money, amount):
        self.vending_machine.insert(money)

        assert self.vending_machine.get_total_amount() == amount

    def test_multiple_insert(self):
        self.vending_machine.insert(Coin10Yen())
        self.vending_machine.insert(Coin50Yen())
        self.vending_machine.insert(Coin100Yen())
        self.vending_machine.insert(Coin500Yen())
        self.vending_machine.insert(Bill1000Yen())

        assert self.vending_machine.get_total_amount() == 1660
