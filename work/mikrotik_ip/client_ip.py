import subprocess
import sys
import socket
import time
import re
import datetime
import http.client
import pyperclip
import threading
import tkinter as tk
import queue
import os.path
import base64
from tkinter import messagebox as mg
from uuid import uuid4
from win32event import CreateMutex
from win32api import CloseHandle, GetLastError
from winerror import ERROR_ALREADY_EXISTS
from pystray import MenuItem, Icon
from PIL import Image

# Класс проверки на запущеную копию
class Singleinstance:
    def __init__(self):
        self.mutexname = "client_ip_{D0E858DF-985E-4907-B7FB-8D732C3FC3B9}"
        self.mutex = CreateMutex(None, False, self.mutexname)
        self.lasterror = GetLastError()

    def aleradyrunning(self):
        return (self.lasterror == ERROR_ALREADY_EXISTS)

    def __del__(self):
        if self.mutex:
            CloseHandle(self.mutex)

# Класс аутентификации нового клиента
class Client_authentication:
    def __init__(self):
        self.key_client = 0

    # GUI для аутентификация
    def authentication_gui(self):
        authentication = tk.Toplevel(root)
        authentication.geometry('300x130')
        x = (authentication.winfo_screenwidth() - authentication.winfo_reqwidth()) / 2
        y = (authentication.winfo_screenheight() - authentication.winfo_reqheight()) / 2
        authentication.wm_geometry("+%d+%d" % (x, y))
        label_authentication = tk.Label(authentication, text='Введите ключ для аутентификации:')
        self.area_authentication = tk.Entry(authentication, bd='2', width=30)
        self.area_authentication.bind("<Control-v>", self.clipboard)
        aply_authentication = tk.Button(authentication, text="Применить ключ", command=self.authentication, width=20)
        cansel = tk.Button(authentication, text='Выход', command=self.quit_gui, width=20)
        label_authentication.place(x=55, y=10)
        self.area_authentication.place(x=60, y=50)
        aply_authentication.place(x=15, y=90)
        cansel.place(x=155, y=90)
        authentication.mainloop()

    def clipboard(self, clip):
        clip = pyperclip.paste()
        # self.area_authentication.delete(0, 'end')
        self.area_authentication.insert(0, clip)

    def quit_gui(self):
        root.destroy()
        sys.exit(0)

    # Обработка аутентификации
    def authentication(self):
        self.key_client = self.area_authentication.get()
        if self.key_client == '':
            mg.showerror('Ошибка', 'Ключ пуст.')
            return
        sock.send(bytes(self.key_client, 'UTF-8'))
        data = sock.recv(1024)
        data = data.decode()
        if data == 'False':
            mg.showerror('Ошибка', 'Ключ не верен.')
            root.destroy()
        else:
            sock.send(bytes(address, 'UTF-8'))
            mg.showinfo('Успешно', 'Добро пожаловать в наши ряды!\nПерезапустите клиент.')
            root.destroy()
            sys.exit(0)

    # Проверка hosts
    def check_host(self):
        reference = []

        with open('C:/Windows/System32/drivers/etc/hosts', 'r') as file:
            file = file.read()

        for i in reference:
            file.rstrip()
            check = bool(file.find(i) + 1)
            if check == False:
                with open('C:/Windows/System32/drivers/etc/hosts', 'a') as f:
                    f.write(i)

# Фоновое выполнение
class Tray:
    def __init__(self):
        self.ip_address_temp = 0

    # Икона в трее
    def tray(self):
        image = Image.open('client_ip.ico')
        menu = (MenuItem('Выход', lambda: self.action_quit()),)
        self.icon = Icon('Client_ip ver 0.3a', image, 'Client_ip ver 0.3a', menu)
        self.icon.run()

    def action_quit(self):
        self.icon.stop()

    def thread_check(self):
        if False == tray.isAlive():
            sys.exit(0)

    def timesleep_thread_check(self):
        count = 0
        while count < 58:
            self.thread_check()
            count += 1
            time.sleep(1)

    def send_info(self):
        # Бесконечный фоновый цикл
        while True:
            time.sleep(3)
            self.timesleep_thread_check()
            self.thread_check()
            conn = http.client.HTTPConnection("ifconfig.me")
            try:
                conn.request("GET", "/ip")
                ip_address = conn.getresponse().read().decode()
            except(TimeoutError):
                continue
            except(OSError):
                continue
            now = datetime.datetime.now().strftime('%H:%M %d-%m-%Y')
            if self.ip_address_temp != ip_address:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((host, port))
                except(ConnectionRefusedError):
                    continue
                except(TimeoutError):
                    continue
                except(OSError):
                    continue
                try:
                    sock.send(bytes(address, 'UTF-8'))
                except(ConnectionRefusedError):
                    continue

                try:
                    data = sock.recv(1024)
                except(OSError):
                    continue

                data = data.decode()
                if 'False' in data:
                    client_authentication.authentication_gui()

                # Записываем в список все данные от хоста
                len_pack = re.findall('\d+', data)
                if not len_pack:
                    continue

                # Условие, если пинг на гугл днс прошел, то выполняем пинг с определеными пакетами и открываем рдп
                # Если пинг не прошел, то пишем ошибку и завершаем скрипт
                if inet == 0:
                    sock.send(bytes('Подтверждение от машины с ID ' + address + ' время ' + now + ' ' + ip_address,
                                    'UTF-8'))
                else:
                    continue

                sock.close()
                self.ip_address_temp = ip_address

if __name__ == '__main__':

    # Наследуем класс ткинтер для отображения GUI и скрываем главное окно
    root = tk.Tk()
    root.geometry('320x250')
    root.title('Client ver. 0.3a')

    # Проверка на копию
    myapp = Singleinstance()
    if myapp.aleradyrunning():
        root.withdraw()
        mg.showinfo('Ошибка', 'Копия программы уже запущена, можно заходить в 1С.')
        sys.exit(0)

    # Окно по центру, в гугле нашел))
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2.5
    root.wm_geometry("+%d+%d" % (x, y))

    label_info = tk.Label(root, font=6, justify='left')
    label_info.grid()
    label_info['text'] += 'Client ver. 0.3a приветствует Вас.\n'
    root.update()
    time.sleep(1)

    # Проверяем hosts
    client_authentication = Client_authentication()
    try:
        client_authentication.check_host()
        label_info['text'] += 'Проверили файл hosts...\n'
    except(PermissionError):
        label_info['text'] += 'Не удалось получить доступ к файлу hosts...\n'
        label_info['text'] += 'Надеемся там все верно...\n'

    # Исходные данные
    tray = Tray()
    conn = http.client.HTTPConnection("ifconfig.me")
    try:
        conn.request("GET", "/ip")
        ip_address = conn.getresponse().read().decode()
    except(TimeoutError):
        mg.showerror('Ошибка', 'Хост 8.8.8.8 не доступен. Нет интернета.')
        sys.exit(0)
    except(OSError):
        mg.showerror('Ошибка', 'Хост 8.8.8.8 не доступен. Нет интернета.')
        sys.exit(0)
    now = datetime.datetime.now().strftime('%H:%M %d-%m-%Y')
    len_pack = []
    google_dns = '8.8.8.8'
    host = ''
    port = ''

    uuid = str(uuid4())
    uuid = uuid.encode('UTF-8')
    uuid = base64.b64encode(uuid)
    uuid = uuid.decode('UTF-8')

    if os.path.isfile('config.cfg') != True:
        with open('config.cfg', 'w') as file:
            file.write(uuid)
        with open('config.cfg', 'r') as file:
            address = file.readlines()
            address = address[0]
            address = address.encode('UTF-8')
            address = base64.b64decode(address)
            address = address.decode('UTF-8')
            address = address[0:18]
    else:
        with open('config.cfg', 'r') as file:
            address = file.readlines()
            address = address[0]
            address = address.encode('UTF-8')
            address = base64.b64decode(address)
            address = address.decode('UTF-8')
            address = address[0:18]

    tray.ip_address_temp = ip_address
    name_client = 'Не_установлено'

    label_info['text'] += 'Проверяем интернет...\n'
    root.update()
    time.sleep(1)

    # Вызов пинга для проверки инета
    inet = subprocess.call(["ping", "-n", "4", google_dns], stdout=False, shell=True)

    if inet == 0:
        label_info['text'] += 'Успешно!\n'
        root.update()
        time.sleep(1)
    else:
        mg.showerror('Ошибка', 'Хост 8.8.8.8 не доступен. Нет интернета.')
        sys.exit(0)

    label_info['text'] += 'Подключаемся к серверу...\n'
    root.update()
    time.sleep(1)

    # Подключаемся в хосту и читаем что он нам передал
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
    except(ConnectionRefusedError):
        mg.showerror('Ошибка', 'Хост ' + host + ' не доступен.')
        sys.exit(0)
    except(TimeoutError):
        mg.showerror('Ошибка', 'Ответ от сервера не получен. Программа завершилась по таймауту.')
        sys.exit(0)
    try:
        sock.send(bytes(address, 'UTF-8'))
    except(ConnectionRefusedError):
        mg.showerror('Ошибка', 'Хост ' + host + ' не доступен.')
        sys.exit(0)
    try:
        data = sock.recv(1024)
    except(OSError):
        mg.showerror('Ошибка', 'Не удалось получить данные с удаленного хоста.')
        sys.exit(0)

    data = data.decode()
    if 'False' in data:
        client_authentication.authentication_gui()

    label_info['text'] += 'Успешно!\n'
    root.update()
    time.sleep(1)

    label_info['text'] += 'Получаем данные от сервера...\n'
    root.update()
    time.sleep(1)

    # Записываем в список все данные от хоста
    len_pack = re.findall('\d+', data)
    if not len_pack:
        mg.showerror('Ошибка', 'Не удалось получить данные с удаленного хоста')
        sys.exit(0)

    # Условие, если пинг на гугл днс прошел, то отправляем внешний айпи-адресс открываем рдп
    # Если пинг не прошел, то пишем ошибку и завершаем скрипт
    if inet == 0:
        sock.send(bytes('Подтверждение от машины с ID ' + address + ' время ' + now + ' ' + ip_address, 'UTF-8'))

        label_info['text'] += 'Успешно!\n'
        root.update()
        time.sleep(0.5)

        label_info['text'] += 'Можно заходить в 1С.\n'
        root.update()

        label_info['text'] += 'Спасибо!\n'
        root.update()

        button_ok = tk.Button(root, text='Закрыть', command=root.destroy, width=10)
        button_ok.place(x=210, y=210)
        root.update()
    else:
        mg.showerror('Ошибка', 'Хост 8.8.8.8 не доступен. Нет интернета.')
        sys.exit(0)

    sock.close()

    root.mainloop()

    send_info = threading.Thread(target=tray.send_info, name='send_info', args=())
    tray = threading.Thread(target=tray.tray, name='tray', args=())
    send_info.start()
    tray.start()
