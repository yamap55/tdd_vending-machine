"""
お金
"""

from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    """
    お金
    """

    @property
    @abstractmethod
    def amount(self):
        """
        金額
        """
        pass


class Coin10Yen(Money):
    """
    10円玉
    """

    amount = 10


class Coin50Yen(Money):
    """
    50円玉
    """

    amount = 50


class Coin100Yen(Money):
    """
    100円玉
    """

    amount = 100


class Coin500Yen(Money):
    """
    500円玉
    """

    amount = 500


class Bill1000Yen(Money):
    """
    1000円札
    """

    amount = 1000
