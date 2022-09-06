# Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention»,
# его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.

# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума max_speed.
# Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.
import time


class Auto(object):
    brand = str
    age = int
    color = str
    mark = str
    weight = int

    def __init__(self, brand, age, mark):
        self.age = age
        self.brand = brand
        self.mark = mark

    def move(self):
        print('«move»')

    def stop(self):
        print('«stop»')

    def birthday(self):
        self.age += 1


class Truck(Auto):
    max_load = int

    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('«attention»')
        super().move()

    def load(self):
        time.sleep(1)
        print('«load»')
        time.sleep(1)


class Car(Auto):
    max_speed = int

    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')


truck_1 = Truck('BMV', 10, 'E100', 5000)
truck_2 = Truck('BMV', 5, 'E23', 10000)
car_1 = Car('BMV', 10, 'E320', 150)
car_2 = Car('Mazda', 7, '450', 180)

truck_1.move()
truck_1.load()
print('-'* 50)

car_1.move()
car_2.move()
car_1.stop()
print(car_2.age)
car_2.birthday()
print(car_2.age)
