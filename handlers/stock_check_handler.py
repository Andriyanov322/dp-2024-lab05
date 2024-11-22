from .base_handler import BaseOrderHandler
from exceptions.out_of_stock_error import OutOfStockError


class StockCheckHandler(BaseOrderHandler):
    """Обработчик для проверки наличия товара на складе."""

    def __init__(self, inventory: dict):
        """
        Args:
            inventory (dict): Информация о наличии товаров на складе.
        """
        super().__init__()
        self.inventory = inventory

    def handle(self, order: dict) -> None:
        """
        Проверяет наличие товара на складе.

        Args:
            order (dict): Данные заказа, включая название товара.

        Raises:
            OutOfStockError: Если товара нет в наличии.
        """
        item = order.get('item')
        if not item or item not in self.inventory or self.inventory[item] == 0:
            raise OutOfStockError(item)
        print(f"StockCheckHandler: Item '{item}' is available.")
        super().handle(order)
