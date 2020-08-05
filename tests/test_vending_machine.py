from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Coin10Yen
import pytest


def test_insert():
    vending_machine = VendingMachine()
    try:
        vending_machine.insert(Coin10Yen())
    except Exception:
        pytest.fail("Unexpected MyError ..")
