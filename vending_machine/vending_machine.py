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
        self.money_box = []
        self.allow_money = (
            Money(10),
            Money(50),
            Money(100),
            Money(500),
            Money(1000),
        )

    @property
    def total(self) -> int:
        """
        投入金額を返す

        Returns
        -------
        int
            投入金額
        """
        return sum(money.amount for money in self.money_box)

    def insert(self, *money_list: Money) -> None:
        """
        お金を投入。

        Parameters
        ----------
        money_list : Money
            投入金額
        """
        for money in money_list:
            if money.amount not in [m.amount for m in self.allow_money]:
                raise ValueError(
                    f"Except money error: {money.amount}, [10, 50, 100, 500, 1000] are available."
                )
        self.money_box += [*money_list]

    def pay_back(self) -> List[Money]:
        """
        投入金額の総計を釣り銭として出力

        Returns
        -------
        Money
            投入金額の総計
        """
        return self.money_box
