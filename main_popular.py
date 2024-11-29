import pandas as pd

# Загрузка данных из файла
df = pd.read_csv('Popularity of Programming Languages from 2004 to 2024.csv')

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Вывод информации о данных
print("\nИнформация о данных:")
print(df.info())

# Вывод статистического описания для колонки Python
print("\nСтатистическое описание для колонки Python:")
print(df['Python'].describe())
