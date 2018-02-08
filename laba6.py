from math import tan, asin

# Класс для результатов
class Result:
    result_g = []
    result_f = []
    result_y = []
    def add_g(self, g):
        self.result_g.append(g)
    def add_f(self, f):
        self.result_f.append(f)
    def add_y(self, y):
        self.result_y.append(y)
    def print_result(self):
        print('G =', *self.result_g)
        if self.result_f == []:
            print('F = нет результатов.')
        else:
            print('F =', *self.result_f)
        if self.result_y == []:
            print('Y = нет результатов.')
        else:
            print('Y =', *self.result_y)

result = Result()

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
    g = 10 * (-45 * a ** 2 + 49 * a * x + 6 * x ** 2) / 15 * a ** 2 + 49 * a * x + 24 * x ** 2
    result.add_g(g)
    try:
        f = tan(5 * a ** 2 + 34 * a * x + 45 * x ** 2)
        result.add_f(f)
    except:
        print('Введенные данные выходят за область значения функции F.')
    try:
        y = -asin(7 * a ** 2 - a * x - 8 * x ** 2)
        result.add_y(y)
    except:
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

print('Результаты:')
print(result.print_result())
