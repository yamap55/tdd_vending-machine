"""飲み物の管理"""


class DrinkBox:
    """
    飲み物の管理
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.inventory = {
            "cola": {
                "amount": 5,
                "price": 120,
            }
        }
