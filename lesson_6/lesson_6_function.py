import random


def casino(counter, number):
    print("Добро пожаловать в казино Hillel\nСтавка - получение 100 балов за ДЗ")
    print(f"У тебя есть {counter} попыток угадать число ")
    while counter != 0:
        input_num = int(input("Введи число: "))
        if input_num == number:
            print("Поздравляю, ты угадал!!!")
            break
        if input_num < number:
            print("Загаданое число больше :) ")
        if input_num > number:
            print("Загаданое число меньше :) ")
        counter -= 1
        print(f"У тебя осталось {counter} попыток")

    if counter == 0:
        print(f"\nДля тебя игра окончена\nЗагаданным числом было {number}")



while True:
    input_counter = input("Введи количество попыток (не больше 7): ")
    if not input_counter.isdigit() or int(input_counter) <= 0 or int(input_counter) > 7:
        print("Некоректный ввод")
        continue
    break

casino(int(input_counter), random.randint(0, 20))
