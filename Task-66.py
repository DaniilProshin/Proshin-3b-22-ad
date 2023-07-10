import sqlite3


conn = sqlite3.connect('students.dp')

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(
   name TEXT,
   age INTEGER,
   average_score REAL
)""")
students = [("PETR", 20, 4.4), ('ANTON', 21, 3), ('KIRILL', 22, 4)]
cursor.executemany("INSERT INTO students VALUES(?, ?, ?);", students)
conn.commit()

cursor.execute("SELECT * FROM students;")
all_students = cursor.fetchall()
for student in all_students:
    print(f'Имя: {student[0]}, Возраст: {student[1]}, Средний балл: {student[2]}')
conn.close()
