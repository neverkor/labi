# Параметры в командкой строке вводятся без запятой, не как в задании, как в задании никто не делает))

# Импортируем библиотеку для обработки аргументов командной строки
import argparse

# Списки для результатов
polynom = []
result = []

# Создаем объект класса
parser = argparse.ArgumentParser()

# Добавляем параметр: --poly - это имя аргумента, nargs - это количество аргументов,
# в данном случае указано что их может быть от 1 и больше, и default - значение аргумента по умолчанию
parser.add_argument('--poly', nargs='+', default='1')

# Помещаем все аргументы в переменую
namespace = parser.parse_args()

# Здесь помещаем все аргументы в список
for poly in namespace.poly:
    polynom.append(float(poly))

# Счетчик
count = 0

# Цикл подсчета, результат помещается в список result
while count < len(polynom):
    x = 1 / polynom[count] * 3
    result.append(x)
    count += 1

# Вывод на экран списка, в котором значения просуммированы
print('Ответ: ', sum(result))
