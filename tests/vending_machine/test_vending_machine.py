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

    # TODO: Refactoring pay_back, (Driver, yamap55)
    @pytest.mark.parametrize("money_list", [[Money.M_10], [Money.M_10, Money.M_1000]])
    def test_pay_back(self, money_list):
        self.vending_machine.insert(*money_list)

        actual = self.vending_machine.pay_back()
        expected = money_list
        assert actual == expected

    def test_check_empty_after_pay_back(self):
        self.vending_machine.insert(Money.M_10)

        self.vending_machine.pay_back()
        actual = self.vending_machine.money_box
        expected = []
        assert actual == expected

    @pytest.mark.parametrize("money", [Money.M_1, Money.M_2000, Money.M_10000])
    def test_insert_except_money(self, money):
        with pytest.raises(ValueError) as excinfo:
            self.vending_machine.insert(money)

        actual = str(excinfo.value)
        expected = f"Except money error: {money.amount}, [10, 50, 100, 500, 1000] are available."
        assert actual == expected
