from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Bill1000, Coin10, Coin50, Coin100
import pytest


class TestInsert:
    @pytest.mark.parametrize(
        "money, money_yen", [(Coin10(), 10), (Coin50(), 50), (Coin100(), 100), (Bill1000(), 1000)]
    )
    def test_insert_money(self, money, money_yen):
        vending_machine = VendingMachine()
        vending_machine.insert(money)

        actual = vending_machine.amount
        expected = money_yen
        assert actual == expected

    def test_insert_multiple_money(self):
        vending_machine = VendingMachine()
        vending_machine.insert(Coin10(), Bill1000())

        actual = vending_machine.amount
        expected = 1010
        assert actual == expected


class TestGetTotalAmount:
    def test_amount_10(self):
        vending_machine = VendingMachine(amount=10)
        actual = vending_machine.get_total_amount()
        expected = 10
        assert actual == expected
