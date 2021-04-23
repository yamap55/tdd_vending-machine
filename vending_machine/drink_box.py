"""飲み物の管理"""


from typing import Any, Dict, List


class DrinkBox:
    """
    飲み物の管理
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.container = {
            "cola": {
                "amount": 5,
                "price": 120,
            }
        }

    def info(self) -> List[Dict[str, Any]]:
        """
        管理している飲み物の情報を返す。

        Returns
        -------
        List[Dict[str, Any]]
            管理している飲み物の情報
        """
        return [{"name": name, **info} for name, info in self.container.items()]
