import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.scatter(x, y, alpha=0.5)
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
