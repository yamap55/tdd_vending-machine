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
