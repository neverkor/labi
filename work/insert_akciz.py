# Вставка символов из файла (в данном случае - акцизных марок) в окно стороней программы (в данном случае - 1с)
# Перед использованием создать ттн исходящую и открыть окно подбор алкогольной продукции
# Далее скрипт вставит все акцизки из указанного файла в ттн
# Пример использования в командной строке: python insert_akciz.py --ins file_name.txt
# Возможно придется указать полные пути до файла
# По умолчанию параметр --ins имеет значение akciz.txt

import win32api, win32con, win32gui, time, win32com.client, argparse, sys

# Функция выбора окна по имени
def open_now(hwnd, windowText):
    if windowText in win32gui.GetWindowText(hwnd):
        win32gui.SetForegroundWindow(hwnd)

# Создаем объект класса argparse
parser = argparse.ArgumentParser(description='Convert text')

# Добавляем параметр --ins
parser.add_argument('--ins', type=str, default='akciz.txt')

# Помещаем все аргументы в переменую
namespace = parser.parse_args()

# Открываем файл для чтения и пишем содержимое в file
try:
    with open(namespace.ins, 'r') as file:
        file = file.readlines()
except(FileNotFoundError):
    print('Ошибка! Файл {} не найден'.format(namespace.ins))
    sys.exit()
except(PermissionError):
    print('Ошибка! Не достаточно прав для открытия файла')
    sys.exit()

# Выбор окна 'Розница'
win32gui.EnumWindows(open_now, 'Розница')

# Эмуляция нажатия клавиш (через shell)
shell = win32com.client.Dispatch('WScript.Shell')

for i in file:
    time.sleep(0.5)
    shell.SendKeys('{F7}')
    time.sleep(0.5)
    shell.SendKeys(i.strip())
    time.sleep(0.5)
    shell.SendKeys('{ENTER}')

print('Выполнено')
