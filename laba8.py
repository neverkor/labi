import itertools
import numpy as np
import matplotlib.pyplot as plt
import time
centr_x = float(input('Введите координату Х для центра окружности: '))
centr_y = float(input('Введите координату Y для центра окружности: '))
radius = float(input('Введите радиус окружности: '))

# Количество точек
point = 150000

# Генерация случайных координат для точек
x = np.random.random_integers(-49, 49, point)
y = np.random.random_integers(-49, 49, point)
result_x = []
result_y = []
os_x = []
os_y = y

# Поиск точек по одной размерности
point_x = float(input('Введите координату X: '))
start = time.time()
for key in x:
    if key == point_x:
        os_x.append(key)
print('На этой координате найдено точек:', len(os_x))
len_x = len(os_x)
if len(os_x) != len(y):
    os_y = os_y[:len_x]
end = time.time()
print('Время выполнения поиска точек:', end - start)

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
print('Центр окружности:', centr_x, ';', centr_y)
print('Точек всего:', point)

# Графическое изображение (не обязательно, так нагляднее)
circle = plt.Circle((centr_x, centr_y), radius, color='blue', fill=False)
fig, ax = plt.subplots()
ax.add_artist(circle)
ax.axis("equal")
plt.xlim(-50, 50)
plt.ylim(-50, 50)
plt.scatter(x, y, s=0.5, color='red')
plt.scatter(os_x, os_y, s=1, color='black')
plt.show()
