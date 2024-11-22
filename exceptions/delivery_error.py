class DeliveryError(Exception):
    """Ошибка при проблемах с доставкой."""

    def __init__(self, address: str):
        """
        Args:
            address (str): Адрес доставки, который вызвал ошибку.
        """
        super().__init__(f"Error: Delivery address '{address}' is missing or invalid.")
