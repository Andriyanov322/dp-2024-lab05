from interfaces.icommand import ICommand
from interfaces.iorder_handler import IOrderHandler


class ProcessOrderCommand(ICommand):
    """Команда для обработки заказа."""

    def __init__(self, handler: IOrderHandler, order: dict):
        """
        Args:
            handler (IOrderHandler): Начальный обработчик цепочки обязанностей.
            order (dict): Данные заказа, включающие товар, оплату и адрес доставки.
        """
        self.handler = handler  # Начальный обработчик цепочки обязанностей
        self.order = order  # Заказ, который нужно обработать

    def execute(self) -> None:
        """
        Запускает выполнение цепочки обязанностей.

        Raises:
            Exception: Любая ошибка, возникшая во время выполнения команды.
        """
        print("ProcessOrderCommand: Executing order processing command.")
        self.handler.handle(self.order)
