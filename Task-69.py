import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
    name TEXT,
    title TEXT,
    salary REAL
)""")

employees = [('Anton', 'manager', 20000), ['Vlad', 'director', 40000],
             ('Irina', 'cleaning', 20000), ('Kirill', 'manager', 20000)]
cursor.executemany("INSERT INTO employees VALUES(?, ?, ?);", employees)
conn.commit()

cursor.execute("SELECT * FROM employees WHERE title='manager';")
all_employees = cursor.fetchall()
for employee in all_employees:
    print(f'Имя: {employee[0]}, Должность: {employee[1]}, Зарплата: {employee[2]}')
conn.close()
