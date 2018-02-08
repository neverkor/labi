from math import tan, asin
a = float(input('Введите А: '))
x = float(input('Введите Х: '))
g = 10 * (-45 * a**2 + 49 * a * x + 6 * x**2) / 15 * a**2 + 49 * a * x +24 * x**2
f = tan(5 * a**2 + 34 * a * x + 45 * x**2)
print('G = {0}, F = {1},'.format(g, f))
a = float(input('Введите А (от -1 до 1): '))
x = float(input('Введите Х (от -1 до 1): '))
y = -asin(7 * a**2 - a * x - 8 * x**2)  # если выражение в скобках меньше -1 и больше 1, вылетает ошибка
print('Y = ', y)
