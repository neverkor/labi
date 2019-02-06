import os, sqlite3, sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
try:
    from scipy.stats import rankdata
except(ModuleNotFoundError):
    messagebox.showerror('Ошибка.', 'Нет модуля Scipy, рейтинг будет работать некорректно. Установите его, написав в '
                                    'командной строке "pip install scipy".')
    sys.exit()

# Основной класс
class Example(tk.Frame):

    # Инициалзируем класс, добавляем кнопки, дерево таблицы в главное окно и атрибуты
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        create_db = tk.Button(self, text='Создать базу SQLite', command=self.create_db)
        delete_db = tk.Button(self, text='Удалить базу SQLite', command=self.delete_db)
        add_note_provider = tk.Button(self, text='Добавить запись в таблицу "Поставщики"',
                                      command=self.add_note_form_provider)
        delete_note_provider = tk.Button(self, width='36', text='Удалить запись в таблице "Поставщики"',
                                         command=self.delete_note_provider)
        show_all_provider = tk.Button(self, width='36', text='Показать все в таблице "Поставщики"',
                                      command=self.show_all_provider)
        show_all_rank = tk.Button(self, width='33', text='Показать все в таблице "Рейтинг"',
                                      command=self.show_all_rank)
        show_all_criterion = tk.Button(self, width='33', text='Показать все в таблице "Критерии"',
                                      command=self.show_all_criterion)
        self.show_all_tree = ttk.Treeview(self, column=('Company', 'Price', 'Deadline',
                                                        'Consignment', 'Delivery', 'Stock',
                                                        'Result', 'Rank'), show='headings')
        self.show_all_tree.column('Company', width=150)
        self.show_all_tree.column('Price', width=100)
        self.show_all_tree.column('Deadline', width=100)
        self.show_all_tree.column('Consignment', width=100)
        self.show_all_tree.column('Delivery', width=100)
        self.show_all_tree.column('Stock', width=100)
        self.show_all_tree.column('Result', width=100)
        self.show_all_tree.column('Rank', width=100)
        create_db.place(x=60, y=10)
        delete_db.place(x=60, y=90)
        add_note_provider.place(x=280, y=10)
        delete_note_provider.place(x=280, y=50)
        show_all_provider.place(x=280, y=90)
        show_all_rank.place(x=600, y=10)
        show_all_criterion.place(x=600, y=90)
        self.show_all_tree.place(x=10, y=130)

    # Метод создания таблицы поставщики
    def create_db(self):

        # Инициализируем подключение к базе
        connect = sqlite3.connect('my_db.db')
        cursor = connect.cursor()

        # Выполняем скрипт SQL для создания всех таблиц
        try:
            cursor.executescript("""CREATE TABLE provider(Company TEXT, Price INTEGER, Deadline INTEGER,
            Consignment INTEGER, Delivery INTEGER, Stock INTEGER);
            INSERT INTO provider (Company, Price, Deadline, Consignment, Delivery, Stock) VALUES ('Комус',
            161, 28, 1, 150, 60);
            INSERT INTO provider (Company, Price, Deadline,Consignment, Delivery, Stock) VALUES ('Ситилинк',
            120, 30, 5, 300, 12);
            INSERT INTO provider (Company, Price, Deadline, Consignment, Delivery, Stock) VALUES ('Supplz',
            562.65, 24, 1, 250, 0);
            INSERT INTO provider (Company, Price, Deadline, Consignment, Delivery, Stock) VALUES ('Yaza',
            204, 24, 1, 50, 5);
            INSERT INTO provider (Company, Price, Deadline, Consignment, Delivery, Stock) VALUES ('Косатка',
            104, 1, 5, 100, 15);
            INSERT INTO provider (Company, Price, Deadline, Consignment, Delivery, Stock) VALUES ('Офси',
            100, 2, 1, 0, 100);
            CREATE TABLE criterion (Criterion_ID INTEGER, Price INTEGER, Deadline INTEGER, Consignment INTEGER,
            Delivery INTEGER, Stock INTEGER);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (1, 100,
            1, 1, 0, 10);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (2, 120,
            3, 2, 50, 20);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (3, 140,
            6, 3, 100, 30);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (4, 160,
            9, 4, 150, 40);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (5, 180,
            12, 5, 200, 50);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (6, 200,
            15, 6, 250, 60);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (7, 220,
            18, 7, 300, 70);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (8, 240,
            21, 8, 350, 80);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (9, 260,
            24, 9, 400, 90);
            INSERT INTO criterion (Criterion_ID, Price, Deadline, Consignment, Delivery, Stock) VALUES (10, 280,
            27, 10, 450, 100);
            CREATE TABLE rank (Company TEXT, Price INTEGER, Deadline INTEGER, Consignment INTEGER, Delivery INTEGER,
            Stock INTEGER, Result INTEGER, Rank INTEGER)""")

            # Подтверждаем изменения
            connect.commit()
            messagebox.showinfo('Успешно.', 'База успешно создана.')
        except(sqlite3.OperationalError):
            messagebox.showerror('Ошибка.', 'База уже создана.')
        except:
            messagebox.showerror('Ошибка.', 'Ошибка не известна.')

        # Закрываем соединения с базой
        connect.close()

    # Метод формы для добвление записи в бд
    def add_note_form_provider(self):

        # Создаем дочернее окно для добавление записей в таблицу поставищики
        self.top = tk.Toplevel(self)
        self.top.geometry('595x150')
        root.eval('tk::PlaceWindow %s' % self.top.winfo_pathname(self.top.winfo_id()))
        label_add_note_form_provider = tk.Label(self.top, text='Введите необходимые данные для добавления в таблицу'
                                                               ' "Поставщики"')
        label_ID = tk.Label(self.top, text='ID')
        self.ID = tk.Entry(self.top, bd='2', width='5')
        label_Company = tk.Label(self.top, text='Наименование')
        self.Company = tk.Entry(self.top, bd='2', width='23')
        label_Price = tk.Label(self.top, text='цена, руб')
        self.Price = tk.Entry(self.top, bd='2', width='10')
        label_Deadline = tk.Label(self.top, text='сроки, ч')
        self.Deadline = tk.Entry(self.top, bd='2', width='10')
        label_Consignment = tk.Label(self.top, text='мин. партия, шт')
        self.Consignment = tk.Entry(self.top, bd='2', width='10')
        label_Delivery = tk.Label(self.top, text='доставка, руб')
        self.Delivery = tk.Entry(self.top, bd='2', width='10')
        label_Stock = tk.Label(self.top, text='склад, шт')
        self.Stock = tk.Entry(self.top, bd='2', width='10')
        create = tk.Button(self.top, text='Добавить', command=self.add_note_provaider)
        label_add_note_form_provider.place(x=100, y=10)
        label_Company.place(x=45, y=50)
        self.Company.place(x=10, y=70)
        label_Price.place(x=180, y=50)
        self.Price.place(x=175, y=70)
        label_Deadline.place(x=270, y=50)
        self.Deadline.place(x=260, y=70)
        label_Consignment.place(x=335, y=50)
        self.Consignment.place(x=345, y=70)
        label_Delivery.place(x=425, y=50)
        self.Delivery.place(x=430, y=70)
        label_Stock.place(x=520, y=50)
        self.Stock.place(x=515, y=70)
        create.place(x=525, y=120)

    # Метод добавления записи в поставищики
    def add_note_provaider(self):

        # Получаем данные из формы добавления записи в таблицу поставщики
        Company_get = self.Company.get()
        Price_get = self.Price.get()
        Deadline_get = self.Deadline.get()
        Consignment_get = self.Consignment.get()
        Delivery_get = self.Delivery.get()
        Stock_get = self.Stock.get()

        # Создаем кортеж с данными из формы
        values = ((Company_get, Price_get, Deadline_get, Consignment_get, Delivery_get, Stock_get))

        # Инициализируем подключение к базе
        connect = sqlite3.connect('my_db.db')
        cursor = connect.cursor()

        # Выполняем команду SQL для добавления в таблицу поставщики, вместо знаков вопроса подставляются данные из
        # кортежа values
        try:
            cursor.execute("INSERT INTO provider VALUES (?, ?, ?, ?, ?, ?)", values)
            # Подтверждаем изменения
            connect.commit()
            messagebox.showinfo('Успешно.', 'Запись успешно добавлена.')
            self.top.destroy()
        except(sqlite3.OperationalError):
            messagebox.showerror('Ошибка.', 'Таблица "Поставщики" не найдена.')
            self.top.destroy()
        except:
            messagebox.showerror('Ошибка.', 'Ошибка не известна.')

        # Закрываем соединения с базой
        connect.close()

    # Метод удаления записи в постащиках
    def delete_note_provider(self):

        # Инициализируем подключение к базе
        connect = sqlite3.connect('my_db.db')
        cursor = connect.cursor()

        # В цикле получаем позицию, которую выделили
        for selected_item in self.show_all_tree.selection():

            # Команда SQL для удаления из таблицы поставщики, вместо вопроса подставляется значение которое выделено
            # в окне
            try:
                cursor.execute("DELETE FROM provider WHERE Company=?", (self.show_all_tree.set(selected_item, '#1'),))
                connect.commit()
                self.show_all_tree.delete(selected_item)
            except(sqlite3.OperationalError):
                messagebox.showerror('Ошибка.', 'Таблица "Поставщики" не найдена.')
            except:
                messagebox.showerror('Ошибка.', 'Ошибка не известна.')

        # Закрываем соединения с базой
        connect.close()

    # Метод показать все что в поставщиках
    def show_all_provider(self):

        # Делаем таблицу в дереве
        self.show_all_tree = ttk.Treeview(self, column=('Company', 'Price', 'Deadline',
                                                        'Consignment', 'Delivery', 'Stock',
                                                        'Result', 'Rank'), show='headings')
        self.show_all_tree.column('Company', width=150, anchor='center')
        self.show_all_tree.column('Price', width=100, anchor='center')
        self.show_all_tree.column('Deadline', width=100, anchor='center')
        self.show_all_tree.column('Consignment', width=100, anchor='center')
        self.show_all_tree.column('Delivery', width=100, anchor='center')
        self.show_all_tree.column('Stock', width=100, anchor='center')
        self.show_all_tree.column('Result', width=100, anchor='center')
        self.show_all_tree.column('Rank', width=100, anchor='center')
        self.show_all_tree.heading('Company', text='Наименование')
        self.show_all_tree.heading('Price', text='Цена, руб')
        self.show_all_tree.heading('Deadline', text='Сроки, ч')
        self.show_all_tree.heading('Consignment', text='Мин. партия, шт')
        self.show_all_tree.heading('Delivery', text='Доставка, руб')
        self.show_all_tree.heading('Stock', text='Склад, шт')

        # Инициализируем подключение к базе
        try:
            connect = sqlite3.connect('my_db.db')
            cursor = connect.cursor()

            # Команда SQL для выбора всего что есть в таблице поставщики
            cursor.execute("SELECT * FROM provider")
            rows = cursor.fetchall()

            # Цикл вставки в дерево значений из кортежа row
            for row in rows:
                self.show_all_tree.insert("", tk.END, values=row)
        except(sqlite3.OperationalError):
            messagebox.showerror('Ошибка.', 'Таблица "Поставщики" не найдена.')
        except:
            messagebox.showerror('Ошибка.', 'Ошибка не известна.')

        # Закрываем соединения с базой
        connect.close()
        self.show_all_tree.place(x=10, y=130)

    # Метод подсчета рейтинга
    def calc_rank(self):

        # Счетчик
        count = 0

        # Создаем пустые списки для подсчетов
        company = []
        price = []
        deadline = []
        consignment = []
        delivery = []
        stock = []
        criterion_price = []
        criterion_deadline = []
        criterion_consignment = []
        criterion_delivery = []
        criterion_stock = []
        rank_price = []
        rank_deadline = []
        rank_consignment = []
        rank_delivery = []
        rank_stock = []
        rank_result = []
        rank = []

        # Инициализируем подключение к базе
        connect = sqlite3.connect('my_db.db')
        cursor = connect.cursor()

        # Очищаем таблицу рейтинг
        cursor.execute("DELETE FROM rank")
        connect.commit()

        # Считаем сколько позиций в таблице поставщики для максимального значения цикла while
        cursor.execute("SELECT COUNT (Company) from provider")
        row_count = cursor.fetchall()
        count_max = row_count[0][0]

        # Выбираем все что есть в столбце компании в таблице поставщиков и записываем в кортеж rows_company
        cursor.execute("SELECT Company FROM provider")
        rows_company = cursor.fetchall()

        # Выбираем все что есть в столбце цена в таблице поставщиков и записываем в кортеж rows_price
        cursor.execute("SELECT Price FROM provider")
        rows_price = cursor.fetchall()

        # Выбираем все что есть в столбце сроки в таблице поставщиков и записываем в кортеж rows_deadline
        cursor.execute("SELECT Deadline FROM provider")
        rows_deadline = cursor.fetchall()

        # Выбираем все что есть в столбце мин партия в таблице поставщиков и записываем в кортеж rows_consignment
        cursor.execute("SELECT Consignment FROM provider")
        rows_consignment = cursor.fetchall()

        # Выбираем все что есть в столбце доставка в таблице поставщиков и записываем в кортеж rows_delivery
        cursor.execute("SELECT Delivery FROM provider")
        rows_delivery = cursor.fetchall()

        # Выбираем все что есть в столбце склад в таблице поставщиков и записываем в кортеж rows_stock
        cursor.execute("SELECT Stock FROM provider")
        rows_stock = cursor.fetchall()

        # Выбираем все что есть в столбце цена в таблице критерии и записываем в кортеж rows_criterion_price
        cursor.execute("SELECT Price FROM criterion")
        rows_criterion_price = cursor.fetchall()

        # Выбираем все что есть в столбце сроки в таблице критерии и записываем в кортеж rows_criterion_deadline
        cursor.execute("SELECT Deadline FROM criterion")
        rows_criterion_deadline = cursor.fetchall()

        # Выбираем все что есть в столбце мин партия в таблице критерии и записываем в кортеж rows_criterion_consignment
        cursor.execute("SELECT Consignment FROM criterion")
        rows_criterion_consignment = cursor.fetchall()

        # Выбираем все что есть в столбце доставка в таблице критерии и записываем в кортеж rows_criterion_delivery
        cursor.execute("SELECT Delivery FROM criterion")
        rows_criterion_delivery = cursor.fetchall()

        # Выбираем все что есть в столбце склад в таблице критерии и записываем в кортеж rows_criterion_stock
        cursor.execute("SELECT Stock FROM criterion")
        rows_criterion_stock = cursor.fetchall()

        # Переносим из всех кортежей которые создали в соответствующие списки
        for i in rows_company:
            company.append(i[0])
        for i in rows_price:
            price.append(i[0])
        for i in rows_deadline:
            deadline.append(i[0])
        for i in rows_consignment:
            consignment.append(i[0])
        for i in rows_delivery:
            delivery.append(i[0])
        for i in rows_stock:
            stock.append(i[0])
        for i in rows_criterion_price:
            criterion_price.append(i[0])
        for i in rows_criterion_deadline:
            criterion_deadline.append(i[0])
        for i in rows_criterion_consignment:
            criterion_consignment.append(i[0])
        for i in rows_criterion_delivery:
            criterion_delivery.append(i[0])
        for i in rows_criterion_stock:
            criterion_stock.append(i[0])

        # Подсчет величины шага критерия для каждой позиции
        criterion_step_price = criterion_price[2] - criterion_price[1]
        criterion_step_deadline = criterion_deadline[2] - criterion_deadline[1]
        criterion_step_consignment = criterion_consignment[2] - criterion_consignment[1]
        criterion_step_delivery = criterion_delivery[2] - criterion_delivery[1]
        criterion_step_stock = criterion_stock[2] - criterion_stock[1]

        # Цикл подсчета рейтинга по формуле 11-а/b, где а - значение из таблицы поставщики, b - шаг критерия
        while count < count_max:
            a_price = price[count] / criterion_step_price
            b_price = 11 - a_price
            rank_price.append(round(b_price))

            a_deadline = deadline[count] / criterion_step_deadline
            b_deadline = 11 - a_deadline
            rank_deadline.append(round(b_deadline))

            a_consignment = consignment[count] / criterion_step_consignment
            b_consignment = 11 - a_consignment
            rank_consignment.append(round(b_consignment))

            a_delivery = delivery[count] / criterion_step_delivery
            b_delivery = 11 - a_delivery
            rank_delivery.append(round(b_delivery))

            a_stock = stock[count] / criterion_step_stock
            rank_stock.append(round(a_stock))

            # Подсчет столбца итого
            rank_result.append(rank_price[count] + rank_deadline[count] + rank_consignment[count]
                               + rank_delivery[count] + rank_stock[count])

            count += 1

        # Обнуляем счетчик
        count = 0

        # Ранжируем результаты
        rank = rankdata(rank_result)

        # Цикл последовательной записи в таблицу рейтинг
        while count < count_max:

            # Кортеж значений
            values = ((company[count], rank_price[count], rank_deadline[count], rank_consignment[count],
                       rank_delivery[count], rank_stock[count], rank_result[count], rank[count]))

            # Запись в SQL в таблицу рейтинг
            cursor.execute("INSERT INTO rank VALUES (?, ?, ?, ?, ?, ?, ?, ?)", values)

            # Подтверждаем изменения
            connect.commit()

            count += 1

        # Закрываем соединения с базой
        connect.close()

    # Метод показать все что в рейтинге
    def show_all_rank(self):

        # Запускаем подсчет
        try:
            self.calc_rank()
        except(sqlite3.OperationalError):
            messagebox.showerror('Ошибка.', 'Таблица "Рейтинг" не найдена.')
        except:
            messagebox.showerror('Ошибка.', 'Ошибка не известна.')

        # Создаем таблицу дерево
        self.show_all_tree = ttk.Treeview(self, column=('Company', 'Price', 'Deadline',
                                                        'Consignment', 'Delivery', 'Stock',
                                                        'Result', 'Rank'), show='headings')
        self.show_all_tree.column('Company', width=150, anchor='center')
        self.show_all_tree.column('Price', width=100, anchor='center')
        self.show_all_tree.column('Deadline', width=100, anchor='center')
        self.show_all_tree.column('Consignment', width=100, anchor='center')
        self.show_all_tree.column('Delivery', width=100, anchor='center')
        self.show_all_tree.column('Stock', width=100, anchor='center')
        self.show_all_tree.column('Result', width=100, anchor='center')
        self.show_all_tree.column('Rank', width=100, anchor='center')
        self.show_all_tree.heading('Company', text='Наименование')
        self.show_all_tree.heading('Price', text='Цена, руб')
        self.show_all_tree.heading('Deadline', text='Сроки, ч')
        self.show_all_tree.heading('Consignment', text='Мин. партия, шт')
        self.show_all_tree.heading('Delivery', text='Доставка, руб')
        self.show_all_tree.heading('Stock', text='Склад, шт')
        self.show_all_tree.heading('Result', text='ИТОГО')
        self.show_all_tree.heading('Rank', text='Рейтинг')

        # Подключаемся к базе
        try:
            connect = sqlite3.connect('my_db.db')
            cursor = connect.cursor()

            # Выбираем все что есть в таблице рейтинга и пишем в кортеж rows
            cursor.execute("SELECT * FROM rank")
            rows = cursor.fetchall()

            # Цикл вывода в таблицу из кортежа
            for row in rows:
                self.show_all_tree.insert("", tk.END, values=row)
        except(sqlite3.OperationalError):
            messagebox.showerror('Ошибка.', 'Таблица "Рейтинг" не найдена.')
        except:
            messagebox.showerror('Ошибка.', 'Ошибка не известна.')

        # Закрываем соединение
        connect.close()
        self.show_all_tree.place(x=10, y=130)

    # Метод показать все что в критериях
    def show_all_criterion(self):

        # Создаем дочернее окно и таблицу дерево
        self.top_1 = tk.Toplevel(self)
        self.top_1.geometry('625x245')
        root.eval('tk::PlaceWindow %s' % self.top_1.winfo_pathname(self.top_1.winfo_id()))
        self.show_all_tree = ttk.Treeview(self.top_1, column=('Criterion_ID', 'Price', 'Deadline',
                                                        'Consignment', 'Delivery', 'Stock'), show='headings')
        self.show_all_tree.column('Criterion_ID', width=100, anchor='center')
        self.show_all_tree.column('Price', width=100, anchor='center')
        self.show_all_tree.column('Deadline', width=100, anchor='center')
        self.show_all_tree.column('Consignment', width=100, anchor='center')
        self.show_all_tree.column('Delivery', width=100, anchor='center')
        self.show_all_tree.column('Stock', width=100, anchor='center')
        self.show_all_tree.heading('Criterion_ID', text='Критерий')
        self.show_all_tree.heading('Price', text='Цена, руб')
        self.show_all_tree.heading('Deadline', text='Сроки, ч')
        self.show_all_tree.heading('Consignment', text='Мин. партия, шт')
        self.show_all_tree.heading('Delivery', text='Доставка, руб')
        self.show_all_tree.heading('Stock', text='Склад, шт')
        self.show_all_tree.place(x=10, y=10)

        # Подключаемся к базе
        try:
            connect = sqlite3.connect('my_db.db')
            cursor = connect.cursor()

            # Выбираем все что есть в таблице критерии и пишем в кортеж rows
            cursor.execute("SELECT * FROM criterion")
            rows = cursor.fetchall()

            # Цикл вывода в таблицу из кортежа
            for row in rows:
                self.show_all_tree.insert("", tk.END, values=row)
        except(sqlite3.OperationalError):
            self.top_1.destroy()
            messagebox.showerror('Ошибка.', 'Таблица "Критерии" не найдена.')
        except:
            self.top_1.destroy()
            messagebox.showerror('Ошибка.', 'Ошибка не известна.')

        # Закрываем соединение
        connect.close()

    # Метод удаления бд
    def delete_db(self):

        # Пытаемся удалить базу физически из системы, если не удачно то переход в ексепт
        try:
            os.remove('my_db.db')
            messagebox.showinfo('Успешно.', 'База удалена.')
        except(PermissionError):
            messagebox.showerror('Ошибка.', 'Нет доступа попобуйте еще раз.')
        except(FileNotFoundError):
            messagebox.showerror('Ошибка.', 'База не найдена.')
        except:
            messagebox.showerror('Ошибка.', 'Ошибка не известна.')

# Тело
if __name__ == "__main__":

    # Инициализируем класс из ткинтера
    root = tk.Tk()

    # Размер окна
    root.geometry('875x375')

    # Название окна
    root.title('Alfa version kis')

    # Окно по центру
    root.eval('tk::PlaceWindow %s' % root.winfo_pathname(root.winfo_id()))

    # Наш класс наследует класс из ткинтера
    Example(root).pack(fill="both", expand=True)

    # Вывод на экран
    root.mainloop()