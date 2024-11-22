from abc import ABC, abstractmethod


class ICommand(ABC):
    """Интерфейс для команд."""

    @abstractmethod
    def execute(self) -> None:
        """
        Выполнить команду.

        Raises:
            Exception: Любая ошибка, возникшая во время выполнения команды.
        """
        pass
