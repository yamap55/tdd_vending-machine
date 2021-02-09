"""
飲み物の自動販売機
"""

from vending_machine.money import Money


class VendingMachine:
    """
    飲み物の自動販売機
    """

    def __init__(self):
        """
        初期処理
        """
        self.total = 0

    def insert(self, *money: Money) -> None:
        """
        お金を投入。

        Parameters
        ----------
        money : Money
            投入金額
        """
        if len(money) == 1:
            return

        total = money[0].amount + money[1].amount
        self.total += total
