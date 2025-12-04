import psycopg2
import re

# -------------------- ПОДКЛЮЧЕНИЕ --------------------

connection = psycopg2.connect(
    database="config",
    user="postgres",
    password="mjkl",
    host="127.0.0.1",
    port="5433"
)

connection.autocommit = True


# -------------------- СОЗДАНИЕ ТАБЛИЦЫ --------------------

def create_table():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phonenumber VARCHAR(20) UNIQUE NOT NULL
            );
        """)
    print("✅ Таблица готова")


# -------------------- 1. ПОИСК ПО ПАТТЕРНУ --------------------

def search_by_pattern(pattern):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT name, phonenumber
            FROM phonebook
            WHERE name ILIKE %s OR phonenumber ILIKE %s
        """, (f"%{pattern}%", f"%{pattern}%"))
        
        return cursor.fetchall()


# -------------------- 2. ВСТАВКА ИЛИ ОБНОВЛЕНИЕ --------------------

def insert_or_update_user(name, phone):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1 FROM phonebook WHERE name = %s", (name,))
        
        if cursor.fetchone():
            cursor.execute(
                "UPDATE phonebook SET phonenumber = %s WHERE name = %s",
                (phone, name)
            )
            print("🔄 Номер обновлён")
        else:
            cursor.execute(
                "INSERT INTO phonebook(name, phonenumber) VALUES (%s, %s)",
                (name, phone)
            )
            print("✅ Пользователь добавлен")


# -------------------- 3. МАССОВАЯ ВСТАВКА С ПРОВЕРКОЙ --------------------

def insert_many_users(users):
    """
    users = [("Ivan", "+77001234567"), ("Bad", "ABC123")]
    """
    invalid = []

    for name, phone in users:

        if not re.fullmatch(r"\+?\d+", phone):
            invalid.append((name, phone))
            continue

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM phonebook WHERE name = %s", (name,))
            if cursor.fetchone():
                cursor.execute(
                    "UPDATE phonebook SET phonenumber = %s WHERE name = %s",
                    (phone, name)
                )
            else:
                cursor.execute(
                    "INSERT INTO phonebook(name, phonenumber) VALUES (%s, %s)",
                    (name, phone)
                )

    return invalid


# -------------------- 4. ПАГИНАЦИЯ --------------------

def get_with_pagination(limit, offset):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT name, phonenumber FROM phonebook
            ORDER BY id
            LIMIT %s OFFSET %s
        """, (limit, offset))

        return cursor.fetchall()


# -------------------- 5. УДАЛЕНИЕ ПО ИМЕНИ ИЛИ ТЕЛЕФОНУ --------------------

def delete_user(value):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM phonebook
            WHERE name = %s OR phonenumber = %s
        """, (value, value))

    print("🗑️ Пользователь удалён")


# -------------------- МЕНЮ --------------------

def menu():
    print("""
1 - Добавить / обновить
2 - Поиск
3 - Массовая вставка
4 - Пагинация
5 - Удаление
6 - Показать всё
0 - Выход
""")


# -------------------- ЗАПУСК --------------------

create_table()

while True:
    menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        phone = input("Телефон: ")
        insert_or_update_user(name, phone)

    elif choice == "2":
        pattern = input("Введите шаблон: ")
        result = search_by_pattern(pattern)
        print(result)

    elif choice == "3":
        users = [
            ("Ivan", "+77001234567"),
            ("Anna", "+77009998877"),
            ("BadGuy", "ABC123")
        ]
        bad = insert_many_users(users)
        print("❌ Некорректные данные:", bad)

    elif choice == "4":
        limit = int(input("LIMIT: "))
        offset = int(input("OFFSET: "))
        print(get_with_pagination(limit, offset))

    elif choice == "5":
        value = input("Имя или телефон: ")
        delete_user(value)

    elif choice == "6":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM phonebook")
            print(cursor.fetchall())

    elif choice == "0":
        break

    else:
        print("❌ Неверный выбор")

connection.close()
print("✅ Соединение закрыто")
