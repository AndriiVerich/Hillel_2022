# Создайте свой произвольный класс и в нём помимо обычных методов и
# атрибутов создайте несколько статических методов и методов класса.
# Продемонстрируйте их работу.
class Product():
    discount = 0

    @staticmethod
    def current_discount():
        print('В нашем магазине представлены товары двух видов')

    def __init__(self, price: int):
        self.price = price

    def total_price(self):
        return  int(self.price - (self.price * Product.discount / 100))

    @classmethod
    def increase_discount(cls):
        cls.discount += 5


a = Product(2000)
b = Product(3000)

a.current_discount()
print('Начальная цена: ', a.total_price())
print('Начальная цена: ', b.total_price())
a.increase_discount()

print('Цена по скидке №1: ',a.total_price())
print('Цена по скидке №1: ',b.total_price())
b.increase_discount()

Product.current_discount()
print('Цена по скидке №2: ', a.total_price())
print('Цена по скидке №2: ', b.total_price())