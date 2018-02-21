import data
import time

# Поиск точек по одной размерности
def search():
    point_x = float(input('Введите координату поиска X: '))
    start = time.time()
    for key in data.x:
        if key == point_x:
            data.os_x.append(key)
    print('На этой координате найдено точек:', len(data.os_x))
    len_x = len(data.os_x)
    if len(data.os_x) != len(data.y):
        data.os_y = data.os_y[:len_x]
    end = time.time()
    data.times.append(end - start)
    print('Время выполнения поиска точек:', *data.times)
