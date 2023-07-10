import sqlite3


conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS books(
    name TEXT,
    author TEXT,
    year INTEGER
)""")
books = [("War and Peace", " Leo Tolstoy", 1869), ("Fairy Tale", 'Stephen King', 2022),
         ('Life of Pee', 'Sally Magnusson', 2009), ('The Master and Margarita', 'Mikhail Bulgakov', 1967)]
cursor.executemany("INSERT INTO books VALUES(?, ?, ?);", books)
conn.commit()

cursor.execute("SELECT * FROM books where year > 2000;")
all_books = cursor.fetchall()
for book in all_books:
    print(f'Название: {book[0]}, Автор: {book[1]}, Год выпуска: {book[2]}')
conn.close()
