# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.


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


avto_1 = Auto("Mazda", 5, "E30")
avto_1.move()
avto_1.stop()
print(avto_1.age)
avto_1.birthday()
print(avto_1.age)
