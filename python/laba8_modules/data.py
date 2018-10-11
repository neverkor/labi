import numpy as np

centr_x = float(input('Введите координату Х для центра окружности: '))
centr_y = float(input('Введите координату Y для центра окружности: '))
radius = float(input('Введите радиус окружности: '))
point = int(input('Введите количество точек: '))
times = []
# Генерация случайных координат для точек
x = np.random.random_integers(-49, 49, point)
y = np.random.random_integers(-49, 49, point)
result_x = []
result_y = []
os_x = []
os_y = y
