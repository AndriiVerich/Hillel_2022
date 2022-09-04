# Прочитать сохранённый json-файл из задания №16 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
import json
import csv
from random import randint

with open('data_file.json') as f:
    output_data_2 = json.load(f)


list_2 = []
for item in (list(output_data_2.items())):
    list_4 = []
    for item_1 in item:
        if isinstance(item_1, str):
            list_4.append(item_1)
        else:
            for item_2 in item_1:
                list_4.append(item_2)
    telephone = str(input(f'Введите телефон {list_4[1]}: '))
    list_4.append(telephone)
    print(list_4)
    list_2.append(list_4)

with open('task_02.csv', mode='w', encoding='utf-8', newline='') as f:
    file_writer = csv.writer(f)
    file_writer.writerow(["Number", "Name", "Age", "Telephone"])
    for item in list_2:
        file_writer.writerow(item)
