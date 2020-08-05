from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Coin10Yen, Coin50Yen, Coin100Yen, Coin500Yen, Bill1000Yen
import pytest


@pytest.mark.parametrize(
    "money", [Coin10Yen(), Coin50Yen(), Coin100Yen(), Coin500Yen(), Bill1000Yen()]
)
def test_insert(money):
    vending_machine = VendingMachine()
    try:
        vending_machine.insert(money)
    except Exception:
        pytest.fail()


def test_multiple_insert():
    vending_machine = VendingMachine()
    try:
        vending_machine.insert(Coin10Yen())
        vending_machine.insert(Coin50Yen())
        vending_machine.insert(Coin100Yen())
        vending_machine.insert(Coin500Yen())
        vending_machine.insert(Bill1000Yen())
    except Exception:
        pytest.fail()
