import data
import calc
import graph
import search

# Поиск точек в окружности
calc.calc()
# Цикл поиска точек по одной размерности и графического изображения
while True:
    search.search()
    graph.graphic()
    # Выход по желанию
    exit_prog = input('Хотите выйти? (y/n): ')
    if 'y' in exit_prog:
        print('Вы вышли из программы.')
        break

# Запись в файл времени выполнения
times = str(data.times)
file = open('time.txt', 'w')
file.write(times)
file.close()
print('Время выполнения записано в файл time.txt')
