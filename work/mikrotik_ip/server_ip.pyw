import sys, socket, threading, sqlite3, re, datetime, logging, hashlib, paramiko, datetime
import tkinter as tk
from tkinter import ttk
from random import randint
from tkinter import messagebox as mg

class Server_ip:
    # Инициалзируем класс, добавляем кнопки, дерево таблицы в главное окно и атрибуты
    def __init__(self):
        self.len_pack = ['50', '100', '150', '200', '250']
        self.name_client = 0
        self.info_tree = 0
        self.data = 0
        self.data_ip_address = 0
        self.flag_mikrotik = 0
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=logging.DEBUG,
                            filename='server_ip.log')

    def gui(self):
        self.root = tk.Tk()
        self.root.geometry('750x260')

        # Окно по центру, в гугле нашел))
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2.5
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2.5
        self.root.wm_geometry("+%d+%d" % (x, y))

        self.root.title('Server ver. 0.1a')
        self.tree = ttk.Treeview(self.root, column=('ID', 'IP', 'Name', 'Confirm', 'Time'), show='headings')
        self.tree.column('ID', width=100, anchor='center')
        self.tree.column('IP', width=100, anchor='center')
        self.tree.column('Name', width=120, anchor='center')
        self.tree.column('Confirm', width=90, anchor='center')
        self.tree.column('Time', width=100, anchor='center')
        self.tree.heading('ID', text='ID')
        self.tree.heading('IP', text='IP-адрес')
        self.tree.heading('Name', text='Имя')
        self.tree.heading('Confirm', text='Подтверждение')
        self.tree.heading('Time', text='Время получения')
        self.delete = tk.Button(self.root, text='Удалить клиента', command=self.delete_client, width=25)
        self.show_all = tk.Button(self.root, text='Показать всех клиентов',command=self.show_all_client, width=25)
        self.view_key_label = tk.Label(self.root, text='Сгенерированный ключ:', width=25)
        self.generate_key = tk.Button(self.root, text='Сгенерировать новый ключ',
                                      command=self.generate_key_client, width=25)
        self.client_info = tk.Label(self.root, text='')
        self.tree.place(x=10, y=10)
        self.show_all.place(x=555, y=15)
        self.delete.place(x=555, y=45)
        self.view_key_label.place(x=555, y=75)
        self.generate_key.place(x=555, y=130)
        self.client_info.place(x=555, y=180)
        self.tree.bind("<Double-1>", self.add_name_client_gui)

        self.create_db()

        self.root.mainloop()

    def create_db(self):
        # Инициализируем подключение к базе
        connect = sqlite3.connect('client.db')
        cursor = connect.cursor()

        # Выполняем команду SQL для создания таблицы
        try:
            cursor.executescript("""CREATE TABLE monitor(ID TEXT, IP TEXT, Name TEXT, Confirm TEXT, Time TEXT);
                                 CREATE TABLE client(ID TEXT);""");

            # Подтверждаем изменения
            connect.commit()
            logging.info('База создана')
        except:
            logging.info('Проверка успешна. База Существует.')
            pass

        # Закрываем соединения с базой
        connect.close()

    # Запись айпи в микротик
    def set_mikrotik_ip(self):
        host_mk = ''
        user_mk = ''
        password_mk = ''
        port_mk = ''
        len_pack_mk = []

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if self.flag_mikrotik == 0:
            try:
                client.connect(hostname=host_mk, username=user_mk, password=password_mk, port=port_mk)
                client.exec_command('ip firewall address-list add address="{}" list="Access_Allow_Test" timeout="12:00:00"'.format(str(self.data_ip_address)))
            except(TimeoutError):
                mg.showerror('Ошибка.', 'Таймаут истек. Микротик не доступен.')
                logging.exception('')
                logging.error('Микротик не доступен.')
            except(paramiko.ssh_exception.NoValidConnectionsError):
                mg.showerror('Ошибка.', 'Микротик не доступен.')
                logging.exception('')
                logging.error('Микротик не доступен.')
        else:
            try:
                client.connect(hostname=host_mk, username=user_mk, password=password_mk, port=port_mk)
                client.exec_command('ip firewall address-list remove [find where list="Access_Allow_Test" && address="{}"]'.format(str(self.ip_client)))
                client.exec_command('ip firewall address-list add address="{}" list="Access_Allow_Test" timeout="12:00:00"'.format(str(self.data_ip_address)))
            except(TimeoutError):
                mg.showerror('Ошибка.', 'Таймаут истек. Микротик не доступен.')
                logging.exception('')
                logging.error('Микротик не доступен.')
            except(paramiko.ssh_exception.NoValidConnectionsError):
                mg.showerror('Ошибка.', 'Микротик не доступен.')
                logging.exception('')
                logging.error('Микротик не доступен.')

        client.close()

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
            cursor.execute("""SELECT * FROM monitor WHERE ID!=1""")
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

    # Метод удаления записи
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
            self.view_pack_4_key.place(x=570, y=100)

    # Метод обработки и отправки пакетов
    def send_info(self):
        flag = 0
        flag_key = 0
        while True:
            try:
                sock.settimeout(5.0)
                conn, addr = sock.accept()
                self.data = conn.recv(1024)
                self.data = self.data.decode()
            except(socket.timeout):
                continue
            except(OSError):
                mg.showerror('Ошибка', 'Не удалось соединиться с клиентом.')
                logging.exception('')
                logging.error('Не удалось соединиться с клиентом.')
                continue

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
                    self.id_client = self.data
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
                self.view_pack_4_key.place(x=570, y=100)

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
                data_time = datetime.datetime.now().strftime('%H:%M %d-%m-%Y')
                self.data_ip_address = data.split()[9]

                # Сравнение айпи клиента из базы
                connect = sqlite3.connect('client.db')
                cursor = connect.cursor()

                try:
                    cursor.execute("""SELECT IP FROM monitor WHERE ID = ?""", (self.id_client,))
                except(sqlite3.OperationalError):
                    mg.showerror('Ошибка.', 'Таблица "Монитор" не найдена.')
                    logging.exception('')
                    logging.error('Таблица "Монитор" не найдена.')

                self.ip_client = cursor.fetchone()

                if self.ip_client == None:
                    self.flag_mikrotik = 0
                    cursor.execute("""INSERT INTO monitor (IP) VALUES (?)""", (self.data_ip_address,))
                    logging.info('Клиент ' + self.id_client + ' сменил айпи адрес, записали запись с IP ' + self.data_ip_address)
                else:
                    for i in self.ip_client:
                        self.ip_client = i

                    values_update_ip = ((self.data_ip_address, self.id_client))

                    if self.ip_client != self.data_ip_address:
                        self.flag_mikrotik = 1
                        cursor.execute("""UPDATE monitor SET IP = ? WHERE ID = ?""", values_update_ip)
                        logging.info('Клиент ' + self.id_client + ' сменил айпи адрес, записали запись с IP ' + self.data_ip_address)

                connect.commit()
                connect.close()

                self.client_info.config(text='Клиент с ID ' + data_id + '\nотправил подтверждение')

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

                connect.close()

            values = ((data_id, self.data_ip_address, self.name_client, confirm, data_time))

            #self.set_mikrotik_ip()

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
                    cursor.execute("""INSERT INTO monitor (ID, IP, Name, Confirm, Time) VALUES (?, ?, ?, ?, ?)""", values)
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

    server = Server_ip()

    # Начальные данные
    host = ''
    port = ''
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
