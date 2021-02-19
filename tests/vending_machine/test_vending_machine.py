import pytest

from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


def test_exists_vending_machine():

    assert VendingMachine()


@pytest.mark.parametrize(
    "amount_list,expected_total",
    [([], 0), ([10], 10), ([10, 50, 100, 500, 1000], 1660)]
    # [10, 50, 100, 500, 1000]
)
def test_insert(amount_list, expected_total):
    money_list = [Money(amount) for amount in amount_list]
    vending_machine = VendingMachine()
    vending_machine.insert(*money_list)
    assert vending_machine.total == expected_total


def test_insert_10():
    money = Money(10)
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


def test_total():
    money1 = Money(10)
    money2 = Money(100)

    vending_machine = VendingMachine()
    vending_machine.insert(money1, money2)

    actual = vending_machine.total
    expected = 110

    assert actual == expected


def test_total_1():
    money1 = Money(10)

    vending_machine = VendingMachine()
    vending_machine.insert(money1)

    actual = vending_machine.total
    expected = 10

    assert actual == expected
