class DeliveryError(Exception):
    """Ошибка при проблемах с доставкой."""
    def __init__(self, address: str):
        super().__init__(f"Error: Delivery address '{address}' is missing or invalid.")
