from datetime import datetime


def my_decorator(in_def):
    start = datetime.now()
    in_def()
    print(f'Время выполнения функции {in_def}:',datetime.now() - start)


@my_decorator
def first_fun():
    print('Hello world')
    for item in range(10000):
         print(item)
    count = 0
    while count <2000:
        count += 1
    print(count)


@my_decorator
def second_fun():
    print('Good morning')
    count = 0
    while count < 20000:
        count +=1
    print(count)
    print(2+4)
