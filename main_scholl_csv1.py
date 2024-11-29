import pandas as pd
import random

# Список учеников и предметов
students = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров']
subjects = ['Математика', 'Литература', 'История', 'Физика', 'Иностранные языки']

# Функция для генерации случайной оценки
def random_grade():
    return pd.Series([random.randint(1, 11) for _ in range(len(subjects))], index=subjects)

# Создаем DataFrame с случайными оценками для каждого ученика
df = pd.DataFrame({student: random_grade() for student in students}).T

# Дублируем имена студентов для примера
df = pd.concat([df] * 2)

# Сохраняем DataFrame в файл CSV
df.to_csv('school.csv', encoding='utf-8')

# Вычисляем среднюю оценку по каждому предмету
average_scores = df.mean()

# Вычисляем медианную оценку по каждому предмету
median_scores = df.median()

# Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

# Вычисляем стандартное отклонение по каждому предмету
std_deviation = df.std()

# Вычисляем IQR для оценок по математике
IQR_math = Q3_math - Q1_math

# Выводим результаты в консоль
print("Средние оценки по предметам:\n", average_scores)
print("\nМедианные оценки по предметам:\n", median_scores)
print("\nQ1 и Q3 для оценок по математике:\nQ1 =", Q1_math, "\nQ3 =", Q3_math)
print("\nСтандартное отклонение по предметам:\n", std_deviation)
print("\nIQR для оценок по математике:\nIQR =", IQR_math)

# Дописываем результаты в DataFrame
df.loc['Средняя оценка'] = average_scores
df.loc['Медианная оценка'] = median_scores
df.loc['Стандартное отклонение'] = std_deviation
df.loc['Q1 (Математика)'] = [Q1_math if subj == 'Математика' else '' for subj in subjects]
df.loc['Q3 (Математика)'] = [Q3_math if subj == 'Математика' else '' for subj in subjects]
df.loc['IQR (Математика)'] = [IQR_math if subj == 'Математика' else '' for subj in subjects]

# Сохраняем DataFrame с результатами в файл CSV
df.to_csv('school.csv', encoding='utf-8')

print("\nРезультаты также записаны в файл school.csv")
