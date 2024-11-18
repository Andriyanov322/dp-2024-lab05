from .base_handler import BaseOrderHandler
from exceptions.out_of_stock_error import OutOfStockError

class StockCheckHandler(BaseOrderHandler):
    """Обработчик для проверки наличия товара на складе."""
    def __init__(self, inventory: dict):
        super().__init__()
        self.inventory = inventory

    def handle(self, order: dict) -> None:
        """Проверяет наличие товара на складе."""
        item = order.get('item')
        if not item or self.inventory.get(item, 0) <= 0:
            raise OutOfStockError(item)
        print(f"StockCheckHandler: Item '{item}' is available.")
        super().handle(order)
