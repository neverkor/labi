import matplotlib.pyplot as plt
import numpy as np

# Списки и словари для результатов
result = []
temp_spam = []
temp_author =[]
temp_from = []
spam = []
author = []
fromm = []
count_spam = []
author_mail = {}
from_mail = {}

# Функция поиска значений спама
def sort_spam():

    # Цикл ищет в файле строку, начинающуюся с X-DSPAM-Confidence: и копирует ее в список
    for i in result:
        if 'X-DSPAM-Confidence:' in i:
            temp_spam.append(i)

    # Цикл записи только значения из строки X-DSPAM-Confidence:
    for i in temp_spam:
        spam.append(float(i[20:]))

    # Среднее значение X-DSPAM-Confidence:
    medium_spam = sum(spam) / len(spam)
    print('Среднее значение параметра X-DSPAM-Confidence: {}\n'.format(medium_spam))

# Функция поиска авторов
def sort_author():

    # Цикл ищет в файле строку, начинающуюся с Author: и копирует ее в список
    for i in result:
        if 'Author:' in i:
            temp_author.append(i)

    # Цикл записи только значения из строки Author:
    for i in temp_author:
        author.append(i[8:-1])

    # Цикл записи в словарь, где ключ - имя автора, а значение - количество писем (повторений)
    for i in author:
        if i in author_mail:
            author_mail[i] += 1
        else:
            author_mail[i] = 1

    # Цикл ищет в файле строку, начинающуюся с From: и копирует ее в список
    for i in result:
        if 'From:' in i:
            temp_from.append(i)

    # Цикл записи только значения из строки From:
    for i in temp_from:
        fromm.append(i[6:-1])

    # Цикл записи в словарь, где ключ - имя автора, а значение - количество писем (повторений)
    for i in fromm:
        if i in from_mail:
            from_mail[i] += 1
        else:
            from_mail[i] = 1

# Функция вывода на экран графика
def graph():

    # Цвет графика
    color_rectangle = np.random.rand(7, 3)

    # Размеры окна, расположение, размер шрифта, название графика и осей
    plt.rcParams['figure.figsize'] = [10, 8]
    plt.rcParams['figure.subplot.left'] = 0.3
    plt.rcParams['font.size'] = 9
    plt.title('Отправители - количество писем')
    plt.xlabel('Письма')

    # Тип графика и данные для построения
    plt.barh(list(from_mail.keys()), list(from_mail.values()), color=color_rectangle)

    # Вывод на экран
    plt.show()

# Основная функция
def main():

    # Открываем файл и читаем построчно в список
    with open('mail_lab_5.txt', 'r') as file:
        for i in file:
            result.append(i)

    # Запуск наших функций
    sort_author()
    sort_spam()

    # Вывод на экран количества элементов спама и авторов, они не сходятся, разница на 1
    print('Почему не выбрал ключевое слово Author? Потому что строк авторов больше на 1 по какой то причине))')
    print('Авторы: {}'.format(len(author)))
    print('X-DSPAM-Confidence: {}\n'.format(len(spam)))

    # Счетчик
    count = 0

    # Кого забанить?
    while count < len(spam):
        if spam[count] == 1:
            print('Бан {}. X-DSPAM-Confidence: {}'.format(fromm[count], spam[count]))
        count += 1

    # Вывод на экран графика
    graph()

if __name__ == '__main__':
    main()
