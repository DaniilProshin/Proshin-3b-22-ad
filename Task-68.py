import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
    name TEXT,
    genre TEXT,
    rating REAL
)""")
movies = [('The Green Mile', 'drama', 9.2), ('It Follows', 'horror', 6.8),
          ('Black Panther', 'adventure', 7.3), ('Step Brothers', 'comedy', 6.9)]
cursor.executemany("INSERT INTO movies VALUES(?, ?, ?);", movies)
conn.commit()


flag = input("Выберите жанр (drama, horror, adventure, comedy): ")
cursor.execute("SELECT * FROM movies;")
all_movies = cursor.fetchall()
for movie in all_movies:
    if movie[1] == flag:
        print(f'Название: {movie[0]}, Жанр: {movie[1]}, Оценка: {movie[2]}')
conn.close()
