# Создать 3 переменные с одинаковыми данными и с одинаковыми идентификаторами
var_1 = "12345"
var_2 = "12345"
var_3 = "12345"
print("Первая часть")
print("Переменные: ", var_1, var_2, var_3)
print('ID :',id(var_1), id(var_2), id(var_3),'\n')
# Поменять их типы так, чтобы у 1-х трёх стали разные идентификаторы, но при этом остались одинаковые данные
var_1 = int(var_1)
var_2 = int(var_2)
var_3 = int(var_3)

print("Переменные: ", var_1, var_2, var_3)
print('ID :',id(var_1), id(var_2), id(var_3),'\n')

#Создать 2 переменные с одинаковыми данными и с разными идентификаторами

a1 = 1
a2 = 1.0
print("Вторая часть")
print('ID:', id(a1))
print('ID:',id(a2))
print('a1 == a2')
print(a1 == a2)
print('a1 is a2')
print(a1 is a2)
a1 = bool(a1)
a2 = bool(a2)
print('ID:', id(a1))
print('ID:',id(a2))
print('a1 == a2')
print(a1 == a2)
print('a1 is a2')
print(a1 is a2)


