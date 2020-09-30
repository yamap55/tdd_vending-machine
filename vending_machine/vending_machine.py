"""自動販売機"""

from .money import Money
from typing import List


class VendingMachine:
    """自動販売機"""

    def __init__(self, money_box: List = None) -> None:
        """初期化処理"""
        self.money_box = money_box if money_box else []

    def insert(self, *moneys: Money) -> None:
        """
        お金投入

        Parameters
        ----------
        money : Money
            投入するお金
        """
        for money in moneys:
            self.money_box.append(money)

    def get_total_amount(self) -> int:
        """投入金額の総計を取得"""
        total = 0
        for money in self.money_box:
            total += money.yen
        return total
