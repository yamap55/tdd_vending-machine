import pytest

from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


class TestVendingMachine:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vending_machine = VendingMachine()

    def test_exists_vending_machine(self):
        assert self.vending_machine

    @pytest.mark.parametrize(
        "amount_list, expected_total", [([], 0), ([10], 10), ([10, 50, 100, 500, 1000], 1660)]
    )
    def test_insert(self, amount_list, expected_total):
        money_list = [Money(amount) for amount in amount_list]

        self.vending_machine.insert(*money_list)
        assert self.vending_machine.total == expected_total

    @pytest.mark.parametrize("money_list", [[Money(10)], [Money(10), Money(1000)]])
    def test_pay_back(self, money_list):
        self.vending_machine.insert(*money_list)

        actual = self.vending_machine.pay_back()
        expected = money_list
        assert actual == expected

    @pytest.mark.parametrize("amount", [(1,), (10000,), (11,)])
    def test_insert_except_money(self, amount):
        with pytest.raises(ValueError) as excinfo:
            self.vending_machine.insert(Money(amount))

        actual = str(excinfo.value)
        expected = f"Except money error: {amount}, [10, 50, 100, 500, 1000] are available."
        assert actual == expected
