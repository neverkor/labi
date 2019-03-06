import matplotlib.pyplot as plt

# Исходные данные (в списке os_y 50 рандомных значений от 0 до 100)
os_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
os_y = [77, 11, 70, 9, 41, 79, 93, 55, 50, 61, 98, 71, 48, 82, 66, 29, 79, 2, 99, 58, 54, 14, 51, 44, 30, 50, 45, 20, 1,
        98, 88, 85, 91, 87, 71, 51, 81, 83, 72, 22, 31, 86, 59, 34, 80, 73, 25, 51, 50, 96]
window = int(input('Введите величину окна: '))
window_temp = window
count = 0
sma = []

# Функция расчета SMA по формуле sma = (p_1 + p_2 + p_3 + ... + p_n) / n
def calc(count, window_temp, window):
    while True:
        sma.append(sum(os_y[count:window_temp])/window)
        count += 1
        window_temp += 1
        if window_temp > len(os_y):
            break
    # Вывод списка SMA для проверки
    # print(sma)

# Функция отображения графиков
def graph(x, y, sma_y):
    plt.title('Самодельная скользящая средняя')
    plt.xlabel('Время')
    plt.ylabel('Значения')
    plt.grid()
    plt.plot(x, y, color='red')
    x = x[:len(sma_y)]
    plt.plot(x, sma_y, color='blue')
    plt.legend(('Основной', 'SMA'))
    plt.show()

# Тело
if __name__ == '__main__':
    calc(count, window_temp, window)
    graph(os_x, os_y, sma)
