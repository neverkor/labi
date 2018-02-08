from math import tan, asin
import pickle

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
    def clean(self):
        self.result_g = []
        self.result_f = []
        self.result_y = []
    def write(self, file):
        pickle.dump(self.result_g, file)
        pickle.dump(self.result_f, file)
        pickle.dump(self.result_y, file)
    def read(self, file):
        self.result_g = pickle.load(file)
        self.result_f = pickle.load(file)
        self.result_y = pickle.load(file)

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

# Открытие файла, запись, чиста списков и чтение из файла
with open('results.txt', 'wb') as file:
    result.write(file)
file.close()
result.clean()
# Можно проверить, очистились списки или нет
#print(result.result_g, result.result_f, result.result_y)
with open('results.txt', 'rb') as file:
    result.read(file)
print(result.print_result())
file.close()
