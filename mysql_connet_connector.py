import os
import io
from mysql.connector import connect, Error
import pickle
from difflib import get_close_matches

def db_mysql_request():
    '''Function connecting to mysql db and return dict with value or None if seach
    result is empty or raise an Error'''

    BD_PASS = os.getenv('BD_PASS')
    # print(BD_PASS)
    try:
        with connect(
                host='192.168.0.110',
                port=3300,
                user='test',
                password=BD_PASS,
                database='egor_db'
        ) as connection:
            print(connection)
            print("Соединение с базой")

            select_req_string = fr'SELECT `Название продукта` FROM Common'

            with connection.cursor() as cr:
                cr.execute(select_req_string)
                req_all = cr.fetchall()
                return req_all


    except Error as e:
        print('Это ошибка', end='')
        print(e)
        return None


if __name__ == '__main__':
    res = db_mysql_request()
    print(len(res))
    #print(res)
    all_products = list(map(lambda x: str(x[0]), res))
    print(all_products)
    test_list = ['Абрикос','Арбуз','Апельсин','Булка']
    print(get_close_matches('белый', all_products, n=5,cutoff=0.5))