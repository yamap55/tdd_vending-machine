import pytest

from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


def test_exists_vending_machine():

    assert VendingMachine()


@pytest.mark.parametrize(
    "amount",
    [
        (10,),
        (50,),
        (100,),
        (500,),
        (1000,),
    ],
)
def test_insert(amount):
    money = Money(amount)
    try:
        VendingMachine().insert(money)
    except AttributeError:
        pytest.fail()


def test_multiple_insert():
    money1 = Money(10)
    money2 = Money(100)

    try:
        VendingMachine().insert(money1, money2)
    except AttributeError:
        pytest.fail()
