from interfaces.icommand import ICommand
from interfaces.iorder_handler import IOrderHandler

class ProcessOrderCommand(ICommand):
    """Команда для обработки заказа."""
    def __init__(self, handler: IOrderHandler, order: dict):
        self.handler = handler  # Начальный обработчик цепочки обязанностей
        self.order = order      # Заказ, который нужно обработать

    def execute(self) -> None:
        """Запускает выполнение цепочки обязанностей."""
        print("ProcessOrderCommand: Executing order processing command.")
        self.handler.handle(self.order)
