"""自動販売機"""

from .money import Money


class VendingMachine:
    """自動販売機"""

    def __init__(self, amount=0) -> None:
        """初期化処理"""
        self.amount = amount

    def insert(self, *moneys: Money) -> None:
        """
        お金投入

        Parameters
        ----------
        money : Money
            投入するお金
        """
        for money in moneys:
            self.amount += money.yen

    def get_total_amount(self) -> int:
        """投入金額の総計を取得"""
        return self.amount
