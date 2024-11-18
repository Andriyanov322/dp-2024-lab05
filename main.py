from handlers import OrderHandler, StockCheckHandler, PaymentProcessorHandler, DeliveryHandler
from commands import ProcessOrderCommand
from exceptions import OutOfStockError, PaymentProcessingError, DeliveryError

# Склад
inventory = {
    'item1': 10,
    'item2': 0,  # Товар отсутствует
}

# Пример заказа
order = {
    'item': 'item1',
    'payment': 100,
    'address': 'UGATU'
}

# Создание цепочки обработчиков
order_handler = OrderHandler()
stock_check_handler = StockCheckHandler(inventory)
payment_processor_handler = PaymentProcessorHandler()
delivery_handler = DeliveryHandler()

# Устанавливаем последовательность обработчиков
order_handler.set_next(stock_check_handler)\
             .set_next(payment_processor_handler)\
             .set_next(delivery_handler)

# Выполнение команды
try:
    command = ProcessOrderCommand(order_handler, order)
    command.execute()
except (OutOfStockError, PaymentProcessingError, DeliveryError) as e:
    print(e)
