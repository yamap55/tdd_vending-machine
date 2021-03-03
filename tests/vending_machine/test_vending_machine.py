import pytest

from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


def test_exists_vending_machine():

    assert VendingMachine()


@pytest.mark.parametrize(
    "amount_list, expected_total", [([], 0), ([10], 10), ([10, 50, 100, 500, 1000], 1660)]
)
def test_insert(amount_list, expected_total):
    money_list = [Money(amount) for amount in amount_list]
    vending_machine = VendingMachine()
    vending_machine.insert(*money_list)
    assert vending_machine.total == expected_total


def test_pay_back():
    vending_machine = VendingMachine()

    insert_money = Money(10)
    vending_machine.insert(insert_money)

    actual = vending_machine.pay_back()
    expected = insert_money
    assert actual == expected
