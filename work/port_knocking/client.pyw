import subprocess, sys, socket, time, re, datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mg
from uuid import getnode

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
        aply_authentication = tk.Button(authentication, text="Применить ключ", command=self.authentication, width=20)
        cansel = tk.Button(authentication, text='Выход', command=root.destroy, width=20)
        label_authentication.place(x=55, y=10)
        self.area_authentication.place(x=60, y=50)
        aply_authentication.place(x=15, y=90)
        cansel.place(x=155, y=90)
        authentication.mainloop()

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

    # Проверка hosts
    def check_host(self):
        reference = ['\n94.181.183.172 srv-ca.disavi.loc', '\n94.181.183.172 srv-rdcb.disavi.loc',
                     '\n94.181.183.172 srv-rdsh1.disavi.loc', '\n94.181.183.172 srv-rdsh2.disavi.loc']

        with open('C:/Windows/System32/drivers/etc/hosts', 'r') as file:
            file = file.read()

        for i in reference:
            file.rstrip()
            check = bool(file.find(i) + 1)
            if check == False:
                with open('C:/Windows/System32/drivers/etc/hosts', 'a') as f:
                    f.write(i)

# Наследуем класс ткинтер для отображения GUI и скрываем главное окно
root = tk.Tk()
root.geometry('320x250')
root.title('Client ver. 0.1a')

# Окно по центру, в гугле нашел))
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2.5
root.wm_geometry("+%d+%d" % (x, y))

label_info = tk.Label(root, font=6, justify='left')
label_info.grid()
label_info['text'] += 'Client ver. 0.1a приветствует Вас.\n'
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
now = datetime.datetime.now().strftime('%H:%M %d-%m-%Y')
len_pack = []
google_dns = '8.8.8.8'
host_mk = '192.168.33.248'
host = '192.168.33.246'
port = 44444
address = str(getnode())
name_client = 'Не_установлено'

label_info['text'] += 'Проверяем интернет...\n'
root.update()
time.sleep(1)

# Вызов пинга для проверки инета
inet = subprocess.call(["ping", "-n", "1", google_dns], stdout=False)

if inet == 0:
    label_info['text'] += 'Успешно!\n'
    root.update()
    time.sleep(1)
else:
    mg.showerror('Ошибка', 'Хост 8.8.8.8 не доступен. Нет интернета.')
    sys.exit()

label_info['text'] += 'Подключаемся к серверу...\n'
root.update()
time.sleep(1)

# Подключаемся в хосту и читаем что он нам передал
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host, port))
except(ConnectionRefusedError):
    mg.showerror('Ошибка', 'Хост ' + host + ' не доступен.')
    sys.exit()
except(TimeoutError):
    mg.showerror('Ошибка', 'Ответ от сервера не получен. Программа завершилась по таймауту.')
    sys.exit()
try:
    sock.send(bytes(address, 'UTF-8'))
except(ConnectionRefusedError):
    mg.showerror('Ошибка', 'Хост ' + host + ' не доступен.')
    sys.exit()
try:
    data = sock.recv(1024)
except(OSError):
    mg.showerror('Ошибка', 'Не удалось получить данные с удаленного хоста.')
    sys.exit()

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
    sys.exit()

label_info['text'] += 'Успешно!\n'
root.update()
time.sleep(1)

label_info['text'] += 'Отправляем пакеты доступа...\n'
root.update()
time.sleep(1)

# Условие, если пинг на гугл днс прошел, то выполняем пинг с определеными пакетами и открываем рдп
# Если пинг не прошел, то пишем ошибку и завершаем скрипт
if inet == 0:
    subprocess.call(["ping", "-n", "1", host_mk, "-l", len_pack[0]], stdout=False)
    subprocess.call(["ping", "-n", "1", host_mk, "-l", len_pack[1]], stdout=False)
    subprocess.call(["ping", "-n", "1", host_mk, "-l", len_pack[2]], stdout=False)
    subprocess.call(["ping", "-n", "1", host_mk, "-l", len_pack[3]], stdout=False)
    subprocess.call(["ping", "-n", "1", host_mk, "-l", len_pack[4]], stdout=False)
    sock.send(bytes('Подтверждение от машины с ID ' + address + ' время ' + now, 'UTF-8'))

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
    sys.exit()

sock.close()

root.mainloop()
