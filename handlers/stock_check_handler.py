from .base_handler import BaseOrderHandler
from exceptions.out_of_stock_error import OutOfStockError


class StockCheckHandler(BaseOrderHandler):
    """Обработчик для проверки наличия товара на складе."""

    def __init__(self, db: dict):
        """
        Args:
            db (dict): "База данных", содержащая информацию о наличии товаров.
        """
        super().__init__()
        self.db = db  # Ссылка на "БД"

    def handle(self, order: dict) -> None:
        """
        Проверяет наличие товара на складе.

        Args:
            order (dict): Данные заказа, включая название товара.

        Raises:
            OutOfStockError: Если товара нет в наличии или название товара некорректно.
        """
        item = order.get('item')

        if not item:
            raise OutOfStockError("Item not specified in the order.")

        # Достаем информацию о наличии товара из "БД"
        stock_count = self.db.get(item, 0)

        if stock_count == 0:
            raise OutOfStockError(item)

        print(f"StockCheckHandler: Item '{item}' is available (Stock: {stock_count}).")
        super().handle(order)
