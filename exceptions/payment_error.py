class PaymentProcessingError(Exception):
    """Ошибка при обработке платежа."""
    def __init__(self, payment: float):
        super().__init__(f"Error: Payment amount '{payment}' is invalid.")
