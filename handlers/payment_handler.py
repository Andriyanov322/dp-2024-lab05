from .base_handler import BaseOrderHandler
from exceptions.payment_error import PaymentProcessingError


class PaymentProcessorHandler(BaseOrderHandler):
    """Обработчик для проверки и выполнения платежа."""

    def handle(self, order: dict) -> None:
        """
        Проверяет корректность платежа.

        Args:
            order (dict): Данные заказа, включая сумму платежа.

        Raises:
            PaymentProcessingError: Если сумма платежа некорректна.
        """
        payment = order.get('payment', 0)
        if payment <= 0:
            raise PaymentProcessingError(payment)
        print(f"PaymentProcessorHandler: Payment processed for '{payment}'.")
        super().handle(order)
