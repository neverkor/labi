# Замена символов с русской раскладки на английскую
# Например есть строка 'ГЫУК'
# После обработки скриптом получается строка 'USER'
# Пример использования в командной строке: python replace_simbol.py --conv file_name.txt
# По умолчанию параметр --conv имеет значение akciz.txt
# Работает только в верхнем регистре букв, так как писалось для конвертации акцизных марок

import argparse
import sys

# Исходные списки
eng = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
       'X', 'C', 'V', 'B', 'N', 'M']
rus = ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Я',
       'Ч', 'С', 'М', 'И', 'Т', 'Ь']

# Пустые списки для результатов
temp_eng = []
eng_final = []
arg = []

# Создаем объект класса argparse
parser = argparse.ArgumentParser(description='Convert text')

# Добавляем параметр: --conv - это имя аргумента, nargs - это количество аргументов,
# в данном случае указано что их может быть от 1 и больше, и default - значение аргумента по умолчанию
parser.add_argument('--conv', type=str, default='akciz.txt')

# Помещаем все аргументы в переменую
namespace = parser.parse_args()

# Открываем файл для чтения и пишем содержимое в lines
try:
    with open(namespace.conv, 'r') as file:
        lines = file.readlines()
except(FileNotFoundError):
    print("Ошибка! Файл {} не найден".format(namespace.conv))
    sys.exit()
except(PermissionError):
    print("Ошибка! Не достаточно прав для открытия файла")
    sys.exit()

# В цикле проходим lines и пишем все элементы в список temp_eng
for i in lines:
    temp = list(i)
    for i in temp:
        temp_eng.append(i)

# В цикле проходим temp_eng и присваиваем simbol значение каждого элемента
for i in temp_eng:
    simbol = i

    # В цикле проходим список rus, получая значение и позицию элемента
    for index, i in enumerate(rus):

        # Сравниваем simbol с элементом из rus, если совпадает, пишем значение с этой же позиции из списка eng
        if simbol == i:
            eng_final.append(eng[index])

    # Если значение simbol есть в списке rus, ниче не делаем, иначе пишем simbol в финальный список eng_final
    # (если simbol нет в rus, это цифра или спецсимвол)
    if simbol in rus:
        pass
    else:
        eng_final.append(simbol)

# Открываем файл на запись и пишем финальный список построчно (если файла нет, он создается)
try:
    with open('akciz_new.txt', 'w') as file:
        file.writelines(eng_final)
except(PermissionError):
    print("Ошибка! Не достаточно прав для создания файла")
    sys.exit()

print('Выполнено')
