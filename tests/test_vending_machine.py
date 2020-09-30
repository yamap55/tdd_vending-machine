from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Bill1000, Coin10, Coin50, Coin100
import pytest


class TestInsert:
    @pytest.mark.parametrize("money", [Coin10(), Coin50(), Coin100(), Bill1000()])
    def test_insert_money(self, money):
        vending_machine = VendingMachine()
        vending_machine.insert(money)

        actual = vending_machine.money_box
        expected = [money]
        assert actual == expected

    def test_insert_multiple_money(self):
        vending_machine = VendingMachine()
        coin10, bill1000 = Coin10(), Bill1000()
        vending_machine.insert(coin10, bill1000)

        actual = vending_machine.money_box
        expected = [coin10, bill1000]
        assert actual == expected


class TestGetTotalAmount:
    def test_amount_10(self):
        vending_machine = VendingMachine(money_box=[Coin10()])
        actual = vending_machine.get_total_amount()
        expected = 10
        assert actual == expected
