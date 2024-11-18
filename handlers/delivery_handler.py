from .base_handler import BaseOrderHandler
from exceptions.delivery_error import DeliveryError

class DeliveryHandler(BaseOrderHandler):
    """Обработчик для доставки товара."""
    def handle(self, order: dict) -> None:
        """Проверяет наличие адреса для доставки."""
        address = order.get('address')
        if not address:
            raise DeliveryError(address)
        print(f"DeliveryHandler: Delivery scheduled to '{address}'.")
        super().handle(order)
