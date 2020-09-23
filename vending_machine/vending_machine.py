"""自動販売機"""

from .money import Money


class VendingMachine:
    """自動販売機"""

    def __init__(self, amount = 0) -> None:
        self.amount = amount

    def insert(self, *money: Money) -> None:
        """
        お金投入

        Parameters
        ----------
        money : List[Money]
            投入するお金
        """
        pass

    def get_total_amount(self) -> int:
        return self.amount
