# Созадать словарь в качестве ключа которого будет 6-ти значное число, а в качестве значений кортеж состоящий
# из 2-х элементов – имя(str), возраст(int). Сделать около 5-6 элементов словаря.
#  Записать данный словарь на диск в json-файл.
import json

def input_str():
    name = input("Введите имя: ").title()
    if name.isdigit():
        return input_str()
    else:
        return name


def input_int():
    age = input("Введите возраст: ")
    if not age.isdigit():
        return input_int()
    else:
        return age


item = 100000
dict_data = {}
while True:
    dict_data[item] = (input_str(), input_int())
    item += 1

    exit_cod = input("Желаете выйти? (Д/Y): ").upper()
    if exit_cod in ("Y", "Д"):
        print(dict_data)
        break

with open("data_file.json", "w") as write_file:
    json.dump(dict_data,write_file)