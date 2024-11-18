import unittest
from handlers import OrderHandler, StockCheckHandler, PaymentProcessorHandler, DeliveryHandler
from commands import ProcessOrderCommand
from exceptions import OutOfStockError, PaymentProcessingError, DeliveryError


class TestOrderProcessing(unittest.TestCase):
    """Тесты для цепочки обязанностей обработки заказов."""

    def setUp(self):
        """Инициализация данных для тестов."""
        self.inventory = {
            'item1': 10,
            'item2': 0  # Товар отсутствует
        }
        self.order = {
            'item': 'item1',
            'payment': 100,
            'address': 'UGATU'
        }

        # Создаем обработчики
        self.order_handler = OrderHandler()
        self.stock_check_handler = StockCheckHandler(self.inventory)
        self.payment_processor_handler = PaymentProcessorHandler()
        self.delivery_handler = DeliveryHandler()

        # Строим цепочку
        self.order_handler.set_next(self.stock_check_handler)\
            .set_next(self.payment_processor_handler)\
            .set_next(self.delivery_handler)

    def test_successful_order(self):
        """Тест успешной обработки заказа."""
        command = ProcessOrderCommand(self.order_handler, self.order)
        try:
            command.execute()
            print("Test passed: successful order.")
        except Exception as e:
            self.fail(f"Test failed: Unexpected exception {e}")

    def test_out_of_stock(self):
        """Тест обработки заказа, если товара нет в наличии."""
        self.order['item'] = 'item2'  # Указываем товар, которого нет на складе
        command = ProcessOrderCommand(self.order_handler, self.order)
        with self.assertRaises(OutOfStockError) as context:
            command.execute()
        self.assertEqual(str(context.exception), "Error: Item 'item2' is out of stock.")

    def test_invalid_payment(self):
        """Тест обработки заказа с некорректным платежом."""
        self.order['payment'] = 0  # Некорректная сумма платежа
        command = ProcessOrderCommand(self.order_handler, self.order)
        with self.assertRaises(PaymentProcessingError) as context:
            command.execute()
        self.assertEqual(str(context.exception), "Error: Payment amount '0' is invalid.")

    def test_missing_address(self):
        """Тест обработки заказа с отсутствующим адресом доставки."""
        self.order.pop('address')  # Удаляем адрес
        command = ProcessOrderCommand(self.order_handler, self.order)
        with self.assertRaises(DeliveryError) as context:
            command.execute()
        self.assertEqual(str(context.exception), "Error: Delivery address 'None' is missing or invalid.")

    def test_partial_chain(self):
        """Тест цепочки, в которой обработчики не все подключены."""
        self.order_handler.set_next(self.stock_check_handler)  # Устанавливаем только проверку наличия
        command = ProcessOrderCommand(self.order_handler, self.order)
        try:
            command.execute()
            print("Test passed: partial chain execution.")
        except Exception as e:
            self.fail(f"Test failed: Unexpected exception {e}")

    def test_item_restocked(self):
        """Тест успешной обработки заказа после пополнения товара."""
        self.order['item'] = 'item2'  # Изначально товар отсутствует
        command = ProcessOrderCommand(self.order_handler, self.order)

        # Первый запуск должен вызвать OutOfStockError
        with self.assertRaises(OutOfStockError):
            command.execute()

        # Пополняем склад
        self.inventory['item2'] = 5

        # Повторная попытка должна пройти успешно
        try:
            command.execute()
            print("Test passed: order processed after restocking.")
        except Exception as e:
            self.fail(f"Test failed: Unexpected exception {e}")


if __name__ == '__main__':
    unittest.main()
