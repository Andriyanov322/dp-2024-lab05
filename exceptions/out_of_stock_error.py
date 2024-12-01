class OutOfStockError(Exception):
    """Ошибка при отсутствии товара на складе."""

    def __init__(self, item: str):
        """
        Args:
            item (str): Название товара, отсутствующего на складе.
        """
        if item:
            super().__init__(f"Error: Item '{item}' is out of stock.")
        else:
            super().__init__("Error: Item not specified in the order.")
