"""自動販売機"""

from .money import Money


class VendingMachine:
    """自動販売機"""

    def insert(self, *money: Money) -> None:
        """
        お金投入

        Parameters
        ----------
        money : List[Money]
            投入するお金
        """
        pass
