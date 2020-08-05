"""
自動販売機
"""


class VendingMachine:
    """
    自動販売機
    """

    total_amount = 0

    def insert(self, money):
        """
        お金を投入

        Parameters
        ----------
        money : Money
            投入
        """
        self.total_amount += money.amount

    def get_total_amount(self) -> int:
        """
        今までに投入された金額の合計を返す

        Returns
        -------
        int
            投入金額
        """
        return self.total_amount
