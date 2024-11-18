from abc import ABC, abstractmethod

class IOrderHandler(ABC):
    """Интерфейс для обработчиков цепочки обязанностей."""
    @abstractmethod
    def set_next(self, handler: 'IOrderHandler') -> 'IOrderHandler':
        """Установить следующий обработчик в цепочке."""
        pass

    @abstractmethod
    def handle(self, order: dict) -> None:
        """Обработать заказ."""
        pass
