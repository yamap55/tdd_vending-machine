import pytest

from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


def test_exists_vending_machine():

    assert VendingMachine()


def test_insert():
    money = Money(100)
    try:
        VendingMachine().insert(money)
    except AttributeError:
        pytest.fail()
