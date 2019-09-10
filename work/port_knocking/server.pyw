import sys, socket, threading, sqlite3, re, datetime, logging, hashlib, paramiko
import tkinter as tk
from tkinter import ttk
from random import randint
from tkinter import messagebox as mg

class Server:
    # Инициалзируем класс, добавляем кнопки, дерево таблицы в главное окно и атрибуты
    def __init__(self):
        self.len_pack = ['50', '100', '150', '200', '250']
        self.name_client = 0
        self.info_tree = 0
        self.data = 0
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=logging.DEBUG,
                            filename='server.log')

    def gui(self):
        self.root = tk.Tk()
        self.root.geometry('800x260')

        # Окно по центру, в гугле нашел))
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2.5
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2.5
        self.root.wm_geometry("+%d+%d" % (x, y))

        self.root.title('Server ver. 0.1a')
        self.tree = ttk.Treeview(self.root, column=('ID', 'Name', 'Confirm', 'Time'), show='headings')
        self.tree.column('ID', width=100, anchor='center')
        self.tree.column('Name', width=120, anchor='center')
        self.tree.column('Confirm', width=90, anchor='center')
        self.tree.column('Time', width=100, anchor='center')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Имя')
        self.tree.heading('Confirm', text='Подтверждение')
        self.tree.heading('Time', text='Время получения')
        self.update_pack = tk.Button(self.root, text='Обновить пакеты', command=self.random_pack, width=20)
        self.view_pack_1 = tk.Label(self.root, text='Текущие пакеты:')
        self.view_pack_2 = tk.Label(self.root, text=self.len_pack)
        self.area_pack_label = tk.Label(self.root, text='Новые пакеты\n (пример: 10 20 30 40 50)')
        self.area_pack = tk.Entry(self.root, bd='2', width='23')
        self.aply_pack = tk.Button(self.root, text='Применить пакеты', command=self.update_len_pack, width=20)
        self.delete = tk.Button(self.root, text='Удалить клиента', command=self.delete_client, width=20)
        self.show_all = tk.Button(self.root, text='Показать всех клиентов',command=self.show_all_client, width=22)
        self.view_pack_3_key = tk.Label(self.root, text='Сгенерированный ключ:')
        self.generate_key = tk.Button(self.root, text='Сгенерировать новый ключ',
                                      command=self.generate_key_client, width=25)
        self.client_info = tk.Label(self.root, text='')
        self.tree.place(x=10, y=10)
        self.delete.place(x=450, y=15)
        self.show_all.place(x=610, y=15)
        self.update_pack.place(x=450, y=50)
        self.view_pack_1.place(x=470, y=80)
        self.view_pack_2.place(x=455, y=100)
        self.area_pack_label.place(x=445, y=135)
        self.area_pack.place(x=440, y=170)
        self.aply_pack.place(x=450, y=200)
        self.view_pack_3_key.place(x=615, y=50)
        self.generate_key.place(x=605, y=110)
        self.client_info.place(x=605, y=160)
        self.create_db()

        connect = sqlite3.connect('client.db')
        cursor = connect.cursor()

        try:
            cursor.execute("""SELECT * FROM packs""")
        except(sqlite3.OperationalError):
            mg.showerror('Ошибка.', 'Таблица "Пакеты" не найдена.')
            logging.exception('')
            logging.error('Таблица "Пакеты" не найдена.')

        self.len_pack = cursor.fetchall()
        if not self.len_pack:
            self.len_pack = [50, 100, 150, 200, 250]
            self.view_pack_2.config(text=self.len_pack)
        else:
            self.view_pack_2.config(text=' '.join(self.len_pack[0]))

        connect.close()

        self.tree.bind("<Double-1>", self.add_name_client_gui)
        self.root.mainloop()

    def create_db(self):
        # Инициализируем подключение к базе
        connect = sqlite3.connect('client.db')
        cursor = connect.cursor()

        # Выполняем команду SQL для создания таблицы
        try:
            cursor.executescript("""CREATE TABLE monitor(ID TEXT, Name TEXT, Confirm TEXT, Time TEXT);
                                 CREATE TABLE packs(Packs INTEGER);
                                 CREATE TABLE client(ID INTEGER);""");

            # Подтверждаем изменения
            connect.commit()
            logging.info('База создана')
        except:
            logging.info('Проверка успешна. База Существует.')
            pass

        # Закрываем соединения с базой
        connect.close()

    # Метод записи в микротик
    def set_mikrotik(self):
        host_mk = '192.168.0.0'
        user_mk = 'admin'
        password_mk = ''
        port_mk = 22
        len_pack_mk = []

        for i in self.len_pack:
            i = int(i)
            i += 28
            len_pack_mk.append(i)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=host_mk, username=user_mk, password=password_mk, port=port_mk)
            client.exec_command('ip firewall filter set packet-size={} numbers=0'.format(str(len_pack_mk[0])))
            client.exec_command('ip firewall filter set packet-size={} numbers=1'.format(str(len_pack_mk[1])))
            client.exec_command('ip firewall filter set packet-size={} numbers=2'.format(str(len_pack_mk[2])))
            client.exec_command('ip firewall filter set packet-size={} numbers=3'.format(str(len_pack_mk[3])))
            client.exec_command('ip firewall filter set packet-size={} numbers=4'.format(str(len_pack_mk[4])))
            self.view_pack_2.config(text=self.len_pack)
        except(TimeoutError):
            mg.showerror('Ошибка.', 'Таймаут истек. Микротик не доступен.')
            logging.exception('')
            logging.error('Микротик не доступен.')
            self.view_pack_2.config(text='{}\n(в микротике не назначено)'.format(self.len_pack))
        except(paramiko.ssh_exception.NoValidConnectionsError):
            mg.showerror('Ошибка.', 'Микротик не доступен.')
            logging.exception('')
            logging.error('Микротик не доступен.')
            self.view_pack_2.config(text='{}\n(в микротике не назначено)'.format(self.len_pack))

        client.close()

    # Метод для обновления пакетов
    def random_pack(self):
        self.len_pack = [randint(1, 2000) for _ in range(5)]
        len_pack_str = [str(item) for item in self.len_pack]
        len_pack_str = ' '.join(len_pack_str)

        # Тут мы записываем в микротик значения из len_pack
        self.set_mikrotik()

        connect = sqlite3.connect('client.db')
        cursor = connect.cursor()

        try:
            cursor.execute("""DELETE FROM packs""")
            cursor.execute("""INSERT INTO packs VALUES ('%s')"""%(len_pack_str))
            logging.info('Обновили записи пакетов')
        except(sqlite3.OperationalError):
            mg.showerror('Ошибка.', 'Таблица "Пакеты" не найдена.')
            logging.exception('')
            logging.error('Таблица "Пакеты" не найдена.')

        connect.commit()
        connect.close()

    # Метод для кнопки применить пакеты
    def update_len_pack(self):
        connect = sqlite3.connect('client.db')
        cursor = connect.cursor()

        self.len_pack = self.area_pack.get()
        if self.len_pack == '':
            mg.showerror('Ошибка.', 'Пустые пакеты, может привести к ошибке в работе!\n'
                                    'Во избежании этого пакеты примут значения по умолчанию.')
            self.len_pack = [50, 100, 150, 200, 250]
            self.set_mikrotik()

            try:
                cursor.execute("""DELETE FROM packs""")
                cursor.execute("""INSERT INTO packs VALUES ('%s')""" % (self.len_pack))
                logging.info('Применили свои записи пакетов')
            except(sqlite3.OperationalError):
                mg.showerror('Ошибка.', 'Таблица "Пакеты" не найдена.')
                logging.exception('')
                logging.error('Таблица "Пакеты" не найдена.')

            connect.commit()
            connect.close()
        else:
            if re.search(r'[^0-9 ]', self.len_pack):
                mg.showerror('Ошибка.', 'Не верные пакеты, может привести к ошибке в работе!\n'
                                    'Во избежании этого пакеты примут значения по умолчанию.')
                self.len_pack = [50, 100, 150, 200, 250]
                self.set_mikrotik()

                try:
                    cursor.execute("""DELETE FROM packs""")
                    cursor.execute("""INSERT INTO packs VALUES ('%s')""" %(self.len_pack))
                    logging.info('Применили свои записи пакетов')
                except(sqlite3.OperationalError):
                    mg.showerror('Ошибка.', 'Таблица "Пакеты" не найдена.')
                    logging.exception('')
                    logging.error('Таблица "Пакеты" не найдена.')

                connect.commit()
                connect.close()

                self.view_pack_2.config(text=self.len_pack)
            else:
                # Тут мы записываем в микротик значения из len_pack
                self.len_pack = self.len_pack.split(' ')
                print(self.len_pack)
                self.set_mikrotik()
                self.len_pack = [int(item) for item in self.len_pack]

                try:
                    cursor.execute("""DELETE FROM packs""")
                    cursor.execute("""INSERT INTO packs VALUES ('%s')""" %(self.len_pack))
                    logging.info('Применили свои записи пакетов')
                except(sqlite3.OperationalError):
                    mg.showerror('Ошибка.', 'Таблица "Пакеты" не найдена.')
                    logging.exception('')
                    logging.error('Таблица "Пакеты" не найдена.')

                connect.commit()
                connect.close()

                self.view_pack_2.config(text=self.len_pack)

    # Метод дочернего окна для изменения имени
    def add_name_client_gui(self, event):
        try:
            self.item = self.tree.selection()[0]
            self.info_tree = self.tree.item(self.item, "values")
        except(IndexError):
            return
        self.add_name_client_gui = tk.Toplevel(self.root)
        self.add_name_client_gui.geometry('200x130')
        x = (self.add_name_client_gui.winfo_screenwidth() - self.add_name_client_gui.winfo_reqwidth()) / 2
        y = (self.add_name_client_gui.winfo_screenheight() - self.add_name_client_gui.winfo_reqheight()) / 2
        self.add_name_client_gui.wm_geometry("+%d+%d" % (x, y))
        label_name = tk.Label(self.add_name_client_gui, text='Введите имя для машины с ID:\n' + self.info_tree[0])
        self.area_name = tk.Entry(self.add_name_client_gui, bd='2', width=25)
        aply_name = tk.Button(self.add_name_client_gui, text="Применить имя", command=self.add_name_client, width=20)
        label_name.place(x=20, y=10)
        self.area_name.place(x=20, y=50)
        aply_name.place(x=35, y=90)
        self.add_name_client_gui.mainloop()

    # Метод изменения имени у клиента
    def add_name_client(self):
        self.name_client = self.area_name.get()
        if self.name_client == '':
            self.name_client = 'Не_установлено'
            self.info_tree = list(self.info_tree)
            self.info_tree[1] = self.name_client
            self.tree.item(self.item, values=self.info_tree)
            self.add_name_client_gui.destroy()
        else:
            self.info_tree = list(self.info_tree)
            self.info_tree[1] = self.name_client
            self.tree.item(self.item, values=self.info_tree)
            self.add_name_client_gui.destroy()

            connect = sqlite3.connect('client.db')
            cursor = connect.cursor()

            values_update = ((self.name_client, self.info_tree[0]))

            try:
                cursor.execute("""UPDATE monitor SET Name = ? WHERE ID = ?""", values_update)
                logging.info('Обновили имя у записи с ID ' + self.info_tree[0])
            except(sqlite3.OperationalError):
                mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                logging.exception('')
                logging.error('Таблица "Монитор" не найдена.')

            connect.commit()

            try:
                cursor.execute("""SELECT Name FROM monitor""")
            except(sqlite3.OperationalError):
                mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                logging.exception('')
                logging.error('Таблица "Монитор" не найдена.')

            row = cursor.fetchall()

            connect.close()

    # Метод показать всех клиентов
    def show_all_client(self):
        connect = sqlite3.connect('client.db')
        cursor = connect.cursor()

        try:
            cursor.execute("""SELECT * FROM monitor""")
            row = cursor.fetchall()
        except(sqlite3.OperationalError):
            mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
            logging.exception('')
            logging.error('Таблица "Монитор" не найдена.')

        for i in self.tree.get_children():
            self.tree.delete(i)

        for i in row:
            self.tree.insert("", tk.END, values=i)

        connect.close()

    # Метод удаления записи в постащиках
    def delete_client(self):

        connect = sqlite3.connect('client.db')
        cursor = connect.cursor()

        for selected_item in self.tree.selection():
            try:
                cursor.execute("""DELETE FROM monitor WHERE ID = ?""", (self.tree.set(selected_item, '#1'),))
                cursor.execute("""DELETE FROM client WHERE ID = ?""", (self.tree.set(selected_item, '#1'),))
                connect.commit()
                logging.info('Удалили запись с ID ' + self.tree.set(selected_item, '#1'))
                self.tree.delete(selected_item)
            except(sqlite3.OperationalError):
                messagebox.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                logging.exception('')
                logging.error('Таблица "Монитор" не найдена.')

        connect.close()

    def generate_key_client(self):
        if not self.data:
            mg.showerror('Ошибка', 'Нет данных для генерации ключа.\nОтправьте данные со стороны клиента.')
        else:
            self.hash_client = hashlib.sha512(b'self.data').hexdigest()
            self.count = 0
            self.key_client = ''
            while self.count < 20:
                self.slice_hash = randint(0, 127)
                self.key_client = self.key_client + self.hash_client[self.slice_hash]
                self.count += 1
            self.key_str = tk.StringVar()
            self.key_str.set(self.key_client)
            self.view_pack_4_key = tk.Entry(self.root, text=self.key_str, state='readonly', justify='center', bd=0)
            self.view_pack_4_key.place(x=615, y=80)

    # Метод обработки и отправки пакетов
    def send_info(self):
        flag = 0
        flag_key = 0
        while True:
            try:
                conn, addr = sock.accept()
                self.data = conn.recv(1024)
                self.data = self.data.decode()
            except(OSError):
                mg.showerror('Ошибка', 'Не удалось соединиться с клиентом.')
                logging.exception('')
                logging.error('Не удалось соединиться с клиентом.')
                break

            # Проверка ID и ключа в базе
            connect = sqlite3.connect('client.db')
            cursor = connect.cursor()

            try:
                cursor.execute("""SELECT ID FROM client""")
            except(sqlite3.OperationalError):
                mg.showerror('Ошибка.', 'Таблица "Клиент" не найдена.')
                logging.exception('')
                logging.error('Таблица "Клиент" не найдена.')

            row = cursor.fetchall()

            connect.close()

            if not row:
                flag_key = 0

            for i in row:
                if self.data in str(i):
                    flag_key = 1
                    break
                else:
                    flag_key = 0

            if flag_key == 0:
                self.hash_client = hashlib.sha512(b'self.data').hexdigest()
                self.count = 0
                self.key_client = ''
                while self.count < 20:
                    self.slice_hash = randint(0, 127)
                    self.key_client = self.key_client + self.hash_client[self.slice_hash]
                    self.count += 1
                self.key_str = tk.StringVar()
                self.key_str.set(self.key_client)
                self.view_pack_4_key = tk.Entry(self.root, text=self.key_str, state='readonly', justify='center', bd=0)
                self.view_pack_4_key.place(x=615, y=80)

                # Отправка 'False', знак того что клиент не прошел фейсконтроль
                conn.send(bytes('False', 'UTF-8'))
                data = conn.recv(1024)
                data = data.decode()
                if not data:
                    continue
                if data != self.key_client:
                    conn.send(bytes('False', 'UTF-8'))
                    continue
                else:
                    conn.send(bytes('True', 'UTF-8'))
                    data = conn.recv(1024)
                    data = data.decode()
                    values = ((data))

                    connect = sqlite3.connect('client.db')
                    cursor = connect.cursor()

                    try:
                        cursor.execute("""INSERT INTO client (ID) VALUES (?)""", (values,))
                        logging.info('Клиент прошел аутентификацию, записали запись с ID ' + data)
                    except(sqlite3.OperationalError):
                        mg.showerror('Ошибка.', 'Таблица "Клиент" не найдена.')
                        logging.exception('')
                        logging.error('Таблица "Клиент" не найдена.')

                    connect.commit()
                    connect.close()

                    self.client_info.config(text='Клиент с ID ' + data + '\nпрошел аутентификацию')

                    continue

                continue
            else:
            # Отправка пакетов
                conn.send(bytes(str(self.len_pack), 'UTF-8'))
                data = conn.recv(1024)
                if data == '':
                    break
                conn.close()

            data = data.decode()
            if not data:
                confirm = 'False'
                data_id = 'Неизвестно'
                data_time = datetime.datetime.now().strftime('%H:%M %d-%m-%Y')
            else:
                confirm = 'True'

                data_id = data.split()[5]
                data_time = data.split()[7] + ' ' + data.split()[8]

                # Установление имени из базы
                connect = sqlite3.connect('client.db')
                cursor = connect.cursor()

                try:
                    cursor.execute("""SELECT Name FROM monitor WHERE ID = ?""", (data_id,))
                except(sqlite3.OperationalError):
                    mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                    logging.exception('')
                    logging.error('Таблица "Монитор" не найдена.')

                self.name_client = cursor.fetchall()
                if self.name_client == []:
                    self.name_client = 'Не_установлено'
                else:
                    pass

                connect.close()

            values = ((data_id, self.name_client, confirm, data_time))

            # Добавление нового клиента или обновление информации о старом клиенте
            connect = sqlite3.connect('client.db')
            cursor = connect.cursor()

            try:
                cursor.execute("""SELECT ID FROM monitor""")
            except(sqlite3.OperationalError):
                mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                logging.exception('')
                logging.error('Таблица "Монитор" не найдена.')

            row = cursor.fetchall()
            values_update = ((data_time, data_id))
            for i in row:
                if data_id in str(i):
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 1:
                values_update = ((data_time, data_id))
                try:
                    cursor.execute("""UPDATE monitor SET Time = ? WHERE ID = ?""", values_update)
                    logging.info('Подключился клиент, обновили запись с ID ' + data_id)
                except(sqlite3.OperationalError):
                    mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                    logging.exception('')
                    logging.error('Таблица "Монитор" не найдена.')
                connect.commit()
            else:
                try:
                    cursor.execute("""INSERT INTO monitor (ID, Name, Confirm, Time) VALUES (?, ?, ?, ?)""", values)
                    logging.info('Подключился клиент, записали запись с ID ' + data_id)
                except(sqlite3.OperationalError):
                    mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                    logging.exception('')
                    logging.error('Таблица "Монитор" не найдена.')
                connect.commit()

            for i in self.tree.get_children():
                self.tree.delete(i)

            try:
                cursor.execute("""SELECT ID FROM monitor""")
            except(sqlite3.OperationalError):
                mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                logging.exception('')
                logging.error('Таблица "Монитор" не найдена.')
            row = cursor.fetchall()

            for i in row:
                try:
                    cursor.execute("""SELECT * FROM monitor WHERE ID = ?""", (i))
                except(sqlite3.OperationalError):
                    mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                    logging.exception('')
                    logging.error('Таблица "Монитор" не найдена.')
                row = cursor.fetchall()
                for i in row:
                    self.tree.insert("", tk.END, values=i)

            connect.close()

# Тело
if __name__ == '__main__':

    server = Server()

    # Начальные данные
    host = '192.168.0.0'
    port = 0
    now = datetime.datetime.now().strftime('%H:%M %d-%m-%Y')

    # Настройка сокета
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((host, port))
        sock.listen(5)
        logging.info('Запуск ' + now)
        logging.info('Заняли IP-адрес ' + str(host) + ', слушаем порт ' + str(port))
    except(OSError):
        mg.showerror('Ошибка', 'Требуемый адрес хоста неверен.')
        logging.exception('')
        logging.error('Требуемый адрес хоста неверен.')
        sys.exit()

    # Создаем два потока, GUI и обработка пакетов
    send_info = threading.Thread(target=server.send_info, name='send_info', daemon=True, args=())
    gui = threading.Thread(target=server.gui, name='gui', args=())
    send_info.start()
    gui.start()
