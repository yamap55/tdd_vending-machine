"""
飲み物の自動販売機
"""

from typing import List

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
        self.money_box = []

    def insert(self, *money_list: Money) -> None:
        """
        お金を投入。

        Parameters
        ----------
        money_list : Money
            投入金額
        """
        self.money_box += [*money_list]
        self.total += sum(money.amount for money in money_list)

    def pay_back(self) -> List[Money]:
        """
        投入金額の総計を釣り銭として出力

        Returns
        -------
        Money
            投入金額の総計
        """
        return self.money_box
