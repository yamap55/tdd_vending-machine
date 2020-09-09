"""自動販売機"""

from .money import Money
from typing import List


class VendingMachine:
    """自動販売機"""

    def insert(self, *money: List[Money]) -> None:
        """
        お金投入

        Parameters
        ----------
        money : List[Money]
            投入するお金
        """
        pass
