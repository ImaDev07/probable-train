# Pandas

# 1 вопрос.
# Series- это одномерный массив данных с индексами
# DataFrame — это таблица в Python, похожая на таблицу в Excel. Она состоит из строк и столбцов,
#а в столбцах могут быть разные типы данных (числа, слова и т.д.)

# 2 вопрос.
# Чтение CSV файла:
# df = pd.read_csv('файл.csv')

# Запись DataFrame в CSV:
# df.to_csv('новый_файл.csv', index=False)

# Индексация:
# df.loc[0]

# Фильтрация:
#выбор строки, где 'age' > 30
# filtered_df = df[df['age'] > 30]

#Группировка:
#группировка по 'name' и подсчет среднего 'age'
# grouped = df.groupby('name')['age'].mean()



# Практика.
import pandas as pd

# Загрузка файла
df = pd.read_csv('movies_ratings.csv')

#фильтрация
movies_after_2000 = df[df['year'] > 2000]
#Средний рейтинг
avg_rating_by_genre = movies_after_2000.groupby('genre')['rating'].mean()

#вывод
top_5_genres = avg_rating_by_genre.sort_values(ascending=False).head(5)

print(top_5_genres)

