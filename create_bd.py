# Создание БД

import sqlite3

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE books (
            name,
            autor,
            description
        )
    """

    cursor.execute(query)