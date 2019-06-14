import matplotlib.pyplot as plt
import numpy as np

class SortMail:
    # Конструктор класса
    def __init__(self):
        self.result = []
        self.temp_spam = []
        self.temp_author = []
        self.temp_from = []
        self.spam = []
        self.author = []
        self.fromm = []
        self.count_spam = []
        self.author_mail = {}
        self.from_mail = {}

    # Метод поиска значений спама
    def sort_spam(self):

        # Цикл ищет в файле строку, начинающуюся с X-DSPAM-Confidence: и копирует ее в список
        for i in self.result:
            if 'X-DSPAM-Confidence:' in i:
                self.temp_spam.append(i)

        # Цикл записи только значения из строки X-DSPAM-Confidence:
        for i in self.temp_spam:
            self.spam.append(float(i[20:]))

        # Среднее значение X-DSPAM-Confidence:
            self.medium_spam = sum(self.spam) / len(self.spam)
        print('Среднее значение параметра X-DSPAM-Confidence: {}\n'.format(self.medium_spam))

    # Метод поиска авторов
    def sort_author(self):

        # Цикл ищет в файле строку, начинающуюся с Author: и копирует ее в список
        for i in self.result:
            if 'Author:' in i:
                self.temp_author.append(i)

        # Цикл записи только значения из строки Author:
        for i in self.temp_author:
            self.author.append(i[8:-1])

        # Цикл записи в словарь, где ключ - имя автора, а значение - количество писем (повторений)
        for i in self.author:
            if i in self.author_mail:
                self.author_mail[i] += 1
            else:
                self.author_mail[i] = 1

        # Цикл ищет в файле строку, начинающуюся с From: и копирует ее в список
        for i in self.result:
            if 'From:' in i:
                self.temp_from.append(i)

        # Цикл записи только значения из строки From:
        for i in self.temp_from:
            self.fromm.append(i[6:-1])

        # Цикл записи в словарь, где ключ - имя автора, а значение - количество писем (повторений)
        for i in self.fromm:
            if i in self.from_mail:
                self.from_mail[i] += 1
            else:
                self.from_mail[i] = 1

    # Метод вывода на экран графика
    def graph(self):

        # Цвет графика
        color_rectangle = np.random.rand(7, 3)

        # Размеры окна, расположение, размер шрифта, название графика и осей
        plt.rcParams['figure.figsize'] = [10, 8]
        plt.rcParams['figure.subplot.left'] = 0.3
        plt.rcParams['font.size'] = 9
        plt.title('Отправители - количество писем')
        plt.xlabel('Письма')

        # Тип графика и данные для построения
        plt.barh(list(self.from_mail.keys()), list(self.from_mail.values()), color=color_rectangle)

        # Вывод на экран
        plt.show()

    # Основной метод
    def main(self):

        # Открываем файл и читаем построчно в список
        with open('mail_lab_5.txt', 'r') as file:
            for i in file:
                self.result.append(i)

        # Запуск наших функций
        self.sort_author()
        self.sort_spam()

        # Вывод на экран количества элементов спама и авторов, они не сходятся, разница на 1
        print('Почему не выбрал ключевое слово Author? Потому что строк авторов больше на 1 по какой то причине))')
        print('Авторы: {}'.format(len(self.author)))
        print('X-DSPAM-Confidence: {}\n'.format(len(self.spam)))

        # Счетчик
        count = 0

        # Кого забанить?
        while count < len(self.spam):
            if self.spam[count] == 1:
                print('Бан {}. X-DSPAM-Confidence: {}'.format(self.fromm[count], self.spam[count]))
            count += 1

        # Вывод на экран графика
        self.graph()

if __name__ == '__main__':
    sortMail = SortMail()
    sortMail.main()
