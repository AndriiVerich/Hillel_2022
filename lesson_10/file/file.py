# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

input_1 = input('Введите что то: ')
input_2 = input('Введите что то: ')
input_3 = input('Введите что то: ')
input_4 = input('Введите что то: ')

file = open('example.txt', 'w')
try:
    file.write(f'{input_1}\n')
    file.write(f'{input_2}\n')
finally:
    file.close()

file = open('example.txt', 'a')
try:
    file.write(f'{input_3}\n')
    file.write(f'{input_4}\n')
finally:
    file.close()
