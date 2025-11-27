import psycopg2


try:
    # connect to exist database
    connection = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="12345", 
        host="127.0.0.1", 
        port="5432"
    )

    connection.autocommit = True

    # the cursor for performing database operations

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")


        #create a table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE snake(
                user_name varchar NOT NULL PRIMARY KEY,
                user_score INTEGER NOT NULL );"""
        )



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")