from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Coin10Yen, Coin50Yen, Coin100Yen, Coin500Yen, Bill1000Yen
import pytest


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
def test_insert(money, amount):
    vending_machine = VendingMachine()
    vending_machine.insert(money)

    assert vending_machine.get_total_amount() == amount


def test_multiple_insert():
    vending_machine = VendingMachine()
    vending_machine.insert(Coin10Yen())
    vending_machine.insert(Coin50Yen())
    vending_machine.insert(Coin100Yen())
    vending_machine.insert(Coin500Yen())
    vending_machine.insert(Bill1000Yen())

    assert vending_machine.get_total_amount() == 1660
