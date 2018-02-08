import itertools
import numpy as np
import matplotlib.pyplot as plt
centr_x = float(input('Введите координату Х для центра окружности: '))
centr_y = float(input('Введите координату Y для центра окружности: '))
radius = float(input('Введите радиус окружности: '))
# Количество точек
N = 1000
# Генерация случайных координат для точек
x = np.random.random_integers(-49, 49, N)
y = np.random.random_integers(-49, 49, N)
result_x = []
result_y = []
# Циклы расчета по формуле (x-centr_x)**2 + (y - centr_y)**2 <= radius**2
for key in x:
    key_x = (key - centr_x)**2
    result_x.append(key_x)
for key in y:
    key_y = (key - centr_y)**2
    result_y.append(key_y)
result = [b+c for b, c in itertools.zip_longest(result_x, result_y, fillvalue=0)]
enter = 0
not_enter = 0
for key in result:
    if key <= radius**2:
        enter += 1
    else:
        not_enter += 1
print('Входит или лежит на окружности точек:', enter, '\nНе входит:', not_enter)
# Графическое изображение (не обязательно, так нагляднее)
circle = plt.Circle((centr_x, centr_y), radius, color='blue', fill=False)
fig, ax = plt.subplots()
ax.add_artist(circle)
ax.axis("equal")
print('Центр окружности:', centr_x, ';', centr_y)
plt.xlim(-50, 50)
plt.ylim(-50, 50)
plt.scatter(x, y, s=7, color='red')
plt.show()
