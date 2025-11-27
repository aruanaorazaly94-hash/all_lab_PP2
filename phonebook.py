import psycopg2

try:

    connection = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="12345", 
        host="127.0.0.1", 
        port="5432"
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")   

        print(f"Server version: {cursor.fetchone()}")

    # #Создание таблицы

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE phonebook(
    #             name varchar NOT NULL,
    #             phonenumber varchar NOT NULL PRIMARY KEY);"""
    #     )

    # Добавление в таблицу из терминала

    # x = str(input())
    # y = str(input())
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         f"""INSERT INTO phonebook (name, phonenumber) VALUES
    #         ('{x}', '{y}');"""
    #     )

    # Добавление в таблицу из csv

    with connection.cursor() as cursor:
                cursor.execute("""COPY phonebook(name, phonenumber)
                                FROM 'C://Users//Public//table.csv'
                                DELIMITER ','
                                CSV HEADER;""")

    # Поиск 

    # choice = str(input())
    # if choice == "phonenumber":
    #     x = str(input())
    #     with connection.cursor() as cursor:
    #         cursor.execute(
    #             f"""SELECT phonenumber FROM phonebook WHERE name = '{x}';"""
    #         )
    #         print(cursor.fetchone())

    # elif choice == "name":
    #     x = str(input())
    #     with connection.cursor() as cursor:
    #         cursor.execute(
    #             f"""SELECT name FROM phonebook WHERE phonenumber = '{x}';"""
    #         )
    #         print(cursor.fetchone())

    # Удаление

    # drop = str(input())
    # with connection.cursor() as cursor:
    #     cursor.execute(f"""DELETE FROM phonebook WHERE name = '{drop}' OR phonenumber = '{drop}'""")                
                


except Exception as _ex:
    print("[INFO] Error while worling with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")