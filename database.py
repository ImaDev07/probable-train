# 2. SQLite

# 1 вопрос.
# SQLite- это встроенная в приложение база данных, которая хранит данные в файле и не требует установки сервера.
# Она используется для хранения и управления данными в небольших приложениях

# 2 вопрос
#CREATE TABLE — создание таблицы
# INSERT — добавление новых записей
# SELECT — выборка данных по условиям
# UPDATE — изменение существующих данных
# DELETE — удаление данных




# Практика.
import sqlite3


conn = sqlite3.connect('sqlite3.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

cursor.execute('INSERT INTO users (name, age) VALUES ('Иман', 22)')
cursor.execute('INSERT INTO users (name, age) VALUES ('Айша', 28)')
cursor.execute('INSERT INTO users (name, age) VALUES ('Максалина', 24)')

cursor.execute('UPDATE users SET age = 26 WHERE id = 1')
cursor.execute('SELECT * FROM users WHERE age > 20')
i = cursor.fetchall()
for i in i:
    print(i)

conn.commit()
conn.close()
