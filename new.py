import psycopg2
from psycopg2 import Error
import pandas as pd
import pandas.io.sql as psql
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="dbinstaller",
                                  # пароль, который указали при установке PostgreSQL
                                  password="dbinstaller",
                                  host="192.168.0.133",
                                  port="5432",
                                  database="uvz")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    # print("Информация о сервере PostgreSQL")
    # print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    print("Схемы и их таблицы")
    cursor.execute("select schemaname, tablename from pg_catalog.pg_tables \
                    where schemaname != 'pg_catalog' \
                    and schemaname !='information_schema' \
                    and schemaname !='public' \
                    order by schemaname;")
    # # Получить результат
    record = cursor.fetchall()
    print(record, "\n")

    schematable = pd.read_sql("select schemaname, tablename from pg_catalog.pg_tables \
                    where schemaname != 'pg_catalog' \
                    and schemaname !='information_schema' \
                    and schemaname !='public' \
                    order by schemaname;", connection)
    print(schematable)
    print("\n\n")

    cursor.execute("select nspname from pg_catalog.pg_namespace \
                    where nspname not in ('pg_toast_temp_1', 'public', 'pg_temp_1', 'pg_catalog', 'information_schema', 'pg_toast');")
    record2 = cursor.fetchall()
    print(record2, "\n")

    for x in testx:
        another_attempt = psql.read_sql("select nspname from pg_catalog.pg_namespace \
        where nspname not in ('pg_toast_temp_1', 'public', 'pg_temp_1', 'pg_catalog', 'information_schema', 'pg_toast');", connection)
        print(testx[x])

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
