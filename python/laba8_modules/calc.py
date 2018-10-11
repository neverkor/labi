import data

# Расчет по формуле (x-centr_x)**2 + (y - centr_y)**2 <= radius**2
def calc():
    for key in data.x:
        key_x = (key - data.centr_x)**2
        data.result_x.append(key_x)
    for key in data.y:
        key_y = (key - data.centr_y)**2
        data.result_y.append(key_y)
    result = list(map(lambda a, b: a + b, data.result_x, data.result_y))
    enter = 0
    not_enter = 0
    for key in result:
        if key <= data.radius**2:
            enter += 1
        else:
            not_enter += 1
    print('Входит или лежит на окружности точек:', enter, '\nНе входит:', not_enter)
    print('Центр окружности:', data.centr_x, ';', data.centr_y)
    print('Точек всего:', data.point)
