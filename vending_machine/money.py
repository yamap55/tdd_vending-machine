"""お金"""


class Money:
    """お金"""
    def __init__(self):
        self.yen = 0


class Bill(Money):
    """お札"""

    pass


class Bill1000(Bill):
    """1000円札"""

    def __init__(self):
        self.yen = 1000


class Coin(Money):
    """硬貨"""

    # 硬貨をインスタンス化して良いのか検討

    pass


class Coin10(Coin):
    """10円硬貨"""

    def __init__(self):
        self.yen = 10


class Coin50(Coin):
    """50円硬貨"""

    def __init__(self):
        self.yen = 50


class Coin100(Coin):
    """100円硬貨"""

    def __init__(self):
        self.yen = 100


class Coin500(Coin):
    """500円硬貨"""

    def __init__(self):
        self.yen = 500
