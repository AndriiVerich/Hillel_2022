# Реализовать функцию, которая выведет прибыль по таблице invoice_items.
#  Сумма по заказу = UnitPrice * Quantity. Если решаем через sql, то нужно использовать sum.
# Результат выполнение функции - одно число, которое является суммой всех заказов.

import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def unwrapper(records: List) -> int:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)


def get_sum_profit() -> None:
    '''
    Функция получения всех записей из таблицы employees
    '''
    query_sql = '''
        SELECT SUM(UnitPrice * Quantity)
          FROM invoice_items;
    '''
    result = execute_query(query_sql)
    unwrapper(result)


get_sum_profit()
