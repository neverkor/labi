from math import tan, asin
a = float(input('Введите А: '))
x = float(input('Введите Х: '))
choose = int(input('1 функция G\n2 функция F\n3 функция Y\nВыберите функцию: '))
if choose == 1:
    try:
        g = 10 * (-45 * a ** 2 + 49 * a * x + 6 * x ** 2) / 0
        print('G =', g)
    except(ZeroDivisionError):
        print('Знаменатель обратился в 0.')
elif choose == 2:
    try:
        f = tan(5 * a ** 2 + 34 * a * x + 45 * x ** 2)
        print('F =', f)
    except(ValueError):
        print('Введенные данные выходят за область значения функции F.')
elif choose == 3:
    try:
        y = -asin(7 * a ** 2 - a * x - 8 * x ** 2)
        print('Y =', y)
    except(ValueError):
        print('Введенные данные выходят за область значения функции Y.')
else:
    print('Нет такой функции.')
