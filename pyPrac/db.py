import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('money.db')
cursor = conn.cursor()

def get_data():
    #запит до бази данних на отримання всіх номіналів, кількість банкнот в яких більше 0
    sql = 'select * from currency where count > 0'
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    return result

def update_count(currency, count, operation):
    '''Обновлення залишків. Функція отримує номінал, кількість і операцю (плюс або мінус) і виконує відповідно додавання
    або відніманя від залишку.'''
    if operation == 'plus':
        sql = 'update currency set count = count + {0} where nominal = {1};'.format(
            count, currency
        )
        cursor.execute(sql)
        conn.commit()
    else:
        sql = 'update currency set count = count - {0} where nominal = {1};'.format(
            count, currency
        )
        cursor.execute(sql)
        conn.commit()