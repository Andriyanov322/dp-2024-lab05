from interfaces.iorder_handler import IOrderHandler


class BaseOrderHandler(IOrderHandler):
    """Базовый класс для реализации цепочки обязанностей."""

    def __init__(self):
        """Инициализация базового обработчика."""
        self._next_handler: IOrderHandler = None

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочке.

        Args:
            handler (IOrderHandler): Следующий обработчик.

        Returns:
            IOrderHandler: Установленный обработчик.
        """
        self._next_handler = handler
        return handler

    def handle(self, order: dict) -> None:
        """
        Передает обработку следующему в цепочке.

        Args:
            order (dict): Данные заказа.
        """
        if self._next_handler:
            self._next_handler.handle(order)
