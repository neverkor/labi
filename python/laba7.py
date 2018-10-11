from math import tan, asin

# Словарь для результатов
result = {'G':[], 'F':[], 'Y':[]}

a = float(input('Введите значения А: '))
x = float(input('Введите минимальное значение X: '))
x_max = float(input('Введите максимальное значение X: '))

# Проверка значений
while x > x_max:
    print('Ошибка! Минимальное значение больше максимального. Повторите ввод.')
    x = float(input('Введите минимальное значение X: '))
    x_max = float(input('Введите максимальное значение X: '))

step = int(input('Введите количество шагов вычисления функции: '))
step_value = float(input('Введите величину шага: '))

# Функция расчета, проверки данных и выводы на экран
def calc(a, x):
    try:
        g = 10 * (-45 * a ** 2 + 49 * a * x + 6 * x ** 2) / 15 * a ** 2 + 49 * a * x + 24 * x ** 2
        result['G'].append(g)
    except(ZeroDivisionError):
        print('Знаменатель обратился в 0.')
    try:
        f = tan(5 * a ** 2 + 34 * a * x + 45 * x ** 2)
        result['F'].append(f)
    except(ValueError):
        print('Введенные данные выходят за область значения функции F.')
    try:
        y = -asin(7 * a ** 2 - a * x - 8 * x ** 2)
        result['Y'].append(y)
    except(ValueError):
        print('Введенные данные выходят за область значения функции Y.')

# Цикл расчета
count = 0
while count < step:
    calc(a, x)
    x += step_value
    if x > x_max:
        print('Ошибка! Величина Х превысила максимальное значение.')
        break
    count += 1

# Запись в файл
with open('result.txt', 'w') as file:
    for key, value in result.items():
        file.write('{} = {}\n' .format(key, value))

# Очистка словаря
result = {}

# Чтение из файла
with open('result.txt', 'r') as file:
    for i in file.readlines():
        key, value = i.strip().split('=')
        print(key, '=', value)
input()
