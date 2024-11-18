from .base_handler import BaseOrderHandler

class OrderHandler(BaseOrderHandler):
    """Первоначальный обработчик заказа."""
    def handle(self, order: dict) -> None:
        """Начинает обработку заказа."""
        print(f"OrderHandler: Starting order processing for {order}.")
        super().handle(order)
