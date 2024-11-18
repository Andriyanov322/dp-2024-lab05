class OutOfStockError(Exception):
    """Ошибка при отсутствии товара на складе."""
    def __init__(self, item: str):
        super().__init__(f"Error: Item '{item}' is out of stock.")
