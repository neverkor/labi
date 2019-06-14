import matplotlib.pyplot as plt
import random

class SMA:
    # Конструктор класса
    def __init__(self, os_x, os_y, window, window_temp, count, sma):
        self.os_x = os_x
        self.os_y = os_y
        self.window = window
        self.window_temp = window_temp
        self.count = count
        self.sma = sma

    # Метод расчета SMA по формуле sma = (p_1 + p_2 + p_3 + ... + p_n) / n
    def calc(self):
        while True:
            self.sma.append(sum(self.os_y[self.count:self.window_temp])/self.window)
            self.count += 1
            self.window_temp += 1
            if self.window_temp > len(self.os_y):
                break
        # Вывод списка SMA для проверки
        # print(self.sma)

    # Метод отображения графиков
    def graph(self):
        plt.title('Самодельная скользящая средняя')
        plt.xlabel('Время')
        plt.ylabel('Значения')
        plt.grid()
        plt.plot(self.os_x, self.os_y, color='red')
        self.os_x = self.os_x[:len(self.sma)]
        plt.plot(self.os_x, self.sma, color='blue')
        plt.legend(('Основной', 'SMA'))
        plt.show()

# Тело
if __name__ == '__main__':

    # Входные данные
    os_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    os_y = random.sample(range(100), 50)
    while True:
        window = int(input('Введите величину окна: '))
        if window == 0:
            print('На ноль делить нельзя. Повторите ввод')
        else:
            break
    window_temp = window
    count = 0
    sma = []

    # Создаем экземпляр класса и выполняем его методы
    smaa = SMA(os_x, os_y, window, window_temp, count, sma)
    smaa.calc()
    smaa.graph()
