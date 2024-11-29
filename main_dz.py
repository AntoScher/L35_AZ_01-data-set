import pandas as pd

# Загружаем данные из файла
"""df = pd.read_csv('dz.csv')
# Заменяем пустые значения на 0
df.fillna(0, inplace=True)
# Определяем среднюю зарплату (Salary) по городу (City)
average_salary_by_city = df.groupby('City')['Salary'].mean()
# Выводим результат
print(average_salary_by_city)"""
import pandas as pd

# Загружаем данные
data = {
    'Name': ['Аня', 'Боб', 'Чарли', 'Лиза', 'Настя', 'Саша', 'Сергей', 'Максим', 'Иван', 'Станислав', 'Вика', 'Мария'],
    'City': ['Томск', 'Москва', 'Москва', 'Томск', None, 'Томск', 'Москва', 'Москва', 'Москва', 'Москва', None, 'Томск'],
    'Salary': [200000, 350000, 270000, 70000, 35000, 23000, 250000, None, 67000, 120000, 47000, 72000]
}
df = pd.DataFrame(data)

# Заменяем пустые значения на 0 для столбца Salary и 'Неизвестно' для столбца City
df.fillna({'City': 'Неизвестно', 'Salary': 0}, inplace=True)

# Определяем пол
female_names = ['Аня', 'Лиза', 'Настя', 'Вика', 'Мария']
male_names = ['Боб', 'Чарли', 'Саша', 'Сергей', 'Максим', 'Иван', 'Станислав']
df['Gender'] = df['Name'].apply(lambda x: 'Female' if x in female_names else 'Male')

# Определяем среднюю зарплату по городу
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Определяем среднюю зарплату для женщин и мужчин
average_salary_by_gender = df.groupby('Gender')['Salary'].mean()

# Выводим все результаты одной командой print
print(f"Средняя зарплата по городу:\n{average_salary_by_city}\n\nСредняя зарплата по полу:\n{average_salary_by_gender}")

