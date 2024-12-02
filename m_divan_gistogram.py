import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла CSV
df = pd.read_csv('svet.csv')

# Вычисление среднего значения
average_price = df['Цена'].mean()
print(f'Средняя цена: {average_price}')

# Создание гистограммы
plt.hist(df['Цена'], bins=30, edgecolor='black', rwidth=0.8)
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.axvline(average_price, color='red', linestyle='dashed', linewidth=1, label=f'Средняя цена: {average_price:.2f}')
plt.legend()
plt.show()
