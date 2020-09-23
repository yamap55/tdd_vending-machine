"""お金"""

from abc import ABC, abstractmethod

class Money(ABC):
    """お金"""
    @property
    @abstractmethod
    def yen(self):
        pass


class Bill(Money):
    """お札"""

    pass


class Bill1000(Bill):
    """1000円札"""
    yen = 1000


class Coin(Money):
    """硬貨"""

    pass


class Coin10(Coin):
    """10円硬貨"""
    yen = 10


class Coin50(Coin):
    """50円硬貨"""
    yen = 50


class Coin100(Coin):
    """100円硬貨"""
    yen = 100


class Coin500(Coin):
    """500円硬貨"""
    yen = 500
