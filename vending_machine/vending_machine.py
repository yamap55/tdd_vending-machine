"""
自動販売機
"""

from typing import List
from .money import Money


class VendingMachine:
    """
    自動販売機
    """

    def __init__(self):
        """初期化処理"""
        self.having_money = []

    def insert(self, money):
        """
        お金を投入

        Parameters
        ----------
        money : Money
            投入
        """
        self.having_money.append(money)

    def get_total_amount(self) -> int:
        """
        今までに投入された金額の合計を返す

        Returns
        -------
        int
            投入金額
        """
        return sum([m.amount for m in self.having_money])

    def refund(self) -> List[Money]:
        """
        今まで投入された金額を払い戻す

        Returns
        -------
        List[Money]
            投入された金額
        """
        return self.having_money
