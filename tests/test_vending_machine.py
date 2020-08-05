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

    def test_refund(self):
        money10 = Coin10Yen()
        money50 = Coin50Yen()
        self.vending_machine.insert(money10)
        self.vending_machine.insert(money50)
        assert self.vending_machine.refund() == [money10, money50]

    def test_not_insert_refund(self):
        assert self.vending_machine.refund() == []

    @pytest.mark.parametrize(
        "insert_item, return_item",
        [
            (Coin10Yen(), None),
            (Coin50Yen(), None),
            (Coin100Yen(), None),
            (Coin500Yen(), None),
            (Bill1000Yen(), None),
            (1, 1),
            ("a", "a"),
            ([], []),
        ],
    )
    def test_insert_return_item(self, insert_item, return_item):
        assert self.vending_machine.insert(insert_item) == return_item
