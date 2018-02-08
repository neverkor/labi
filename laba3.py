from math import tan, asin
a = float(input('Введите значения А: '))
x_min = float(input('Введите минимальное значение X: '))
x_max = float(input('Введите максимальное значение X: '))

# Проверка значений
while x_min > x_max:
    print('Ошибка! Минимальное значение {0} больше максимального {1}. Повторите ввод.'.format(x_min, x_max))
    x_min = float(input('Введите минимальное значение X: '))
    x_max = float(input('Введите максимальное значение X: '))

step = int(input('Введите количество шагов вычисления функции: '))
step_value = float(input('Введите величину шага: '))
choose = int(input('1 функция G\n2 функция F\n3 функция Y\nВыберите функцию: '))
x = x_min

# Функция расчета, проверки данных и выводы на экран
def calc(a, x):
    if choose == 1:
        g = 10 * (-45 * a ** 2 + 49 * a * x + 6 * x ** 2) / 15 * a ** 2 + 49 * a * x + 24 * x ** 2
        print('G =', g)
    elif choose == 2:
        try:
            f = tan(5 * a ** 2 + 34 * a * x + 45 * x ** 2)
            print('F =', f)
        except:
            print('Введенные данные выходят за область значения функции.')
    elif choose == 3:
        try:
            y = -asin(7 * a ** 2 - a * x - 8 * x ** 2)
            print('Y =', y)
        except:
            print('Введенные данные выходят за область значения функции.')
    else:
        print('Нет такой функции.')

# Цикл расчета
count = 0
while count < step:
    calc(a, x)
    x += step_value
    if x > x_max:
        print('Ошибка! Величина Х превысила максимальное значение.')
        break
    count += 1
    
