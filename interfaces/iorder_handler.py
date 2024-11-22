from abc import ABC, abstractmethod


class IOrderHandler(ABC):
    """Интерфейс для обработчиков цепочки обязанностей."""

    @abstractmethod
    def set_next(self, handler: 'IOrderHandler') -> 'IOrderHandler':
        """
        Установить следующий обработчик в цепочке.

        Args:
            handler (IOrderHandler): Следующий обработчик в цепочке обязанностей.

        Returns:
            IOrderHandler: Установленный следующий обработчик.
        """
        pass

    @abstractmethod
    def handle(self, order: dict) -> None:
        """
        Обработать заказ.

        Args:
            order (dict): Словарь с данными заказа, включающий информацию о товаре, платеже и адресе.
        """
        pass
