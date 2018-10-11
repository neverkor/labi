import os, sys, shutil, ctypes, tkinter
from tkinter import messagebox
from tkinter import filedialog as fd

# Упаковка в EXE
def packing_exe():
    if sys.platform == 'win32':
        import os
        command1 = 'pip install wheel'
        command2 = 'pip install pyinstaller'
        command3 = 'pyinstaller --onedir --onefile --name=backup d:/backup_python/backup.pyw'
        os.system(command1)
        os.system(command2)
        os.system(command3)
        shutil.copy2(src, dst)
        shutil.rmtree(os.path.realpath('./build'))
        shutil.rmtree(os.path.realpath('./dist'))
        shutil.rmtree(os.path.realpath('./__pycache__'))
        messagebox.showinfo('Успешно.', 'Скрипт упакован в EXE и помещен в ' + os.path.realpath('./'))
    else:
        messagebox.showinfo('Ошибка.', 'У вас установлена не ОС Windows')

# Очистка полей ввода e-mail
def delete_data_email():
    data_my_email.delete(0, 1000)
    data_you_email.delete(0, 1000)
    data_password.delete(0, 1000)

# Сохранить e-mail
def save_email():
    my_email = data_my_email.get()
    you_email = data_you_email.get()
    password = data_password.get()
    serv_smtp = data_serv_smtp.get()
    port_smtp = data_port_smtp.get()
    if my_email == '' or you_email == '':
        with open('backup.conf', 'r') as file:
            lines = file.readlines()
        lines[1] = 'My_email = ' + my_email + '\n'
        lines[5] = 'You_email = ' + you_email + '\n'
        with open('backup.conf', 'w') as file:
            file.writelines(lines)
        messagebox.showinfo('Успешно.', 'Функция отправки письма отключена')
    elif '@' not in my_email:
        messagebox.showerror('Ошибка.', 'Неверный e-mail ' + my_email)
    elif password == '':
        messagebox.showerror('Ошибка', 'Пустой пароль')
    elif '@' not in you_email:
        messagebox.showerror('Ошибка.', 'Неверный e-mail ' + you_email)
    else:
        with open('backup.conf', 'r') as file:
            lines = file.readlines()
        lines[1] = 'My_email = ' + my_email + '\n'
        lines[2] = 'Password = ' + password + '\n'
        if serv_smtp == '':
            lines[3] = 'Server SMTP = smtp.gmail.com' + serv_smtp + '\n'
        else:
            lines[3] = 'Server SMTP = ' + serv_smtp + '\n'
        if port_smtp == '':
            lines[4] = 'Port SMTP = 587\n'
        else:
            lines[4] = 'Port SMTP = ' + port_smtp + '\n'
        lines[5] = 'You_email = ' + you_email + '\n'
        with open('backup.conf', 'w') as file:
            file.writelines(lines)
        messagebox.showinfo('Успешно.', 'Сохранено ' + my_email + ' и ' + you_email)

# Обзор для ввода пути
def review():
    file_name = fd.askopenfilename()
    data_dir.delete(0, 1000)
    data_dir.insert(0, file_name)

# Сохранить путь
def save():
    data_file = data_dir.get()
    if data_file == '':
        messagebox.showerror('Ошибка.', 'Пустой путь')
    elif '\\' in data_file:
        data_file.replace('\\', '/')
        with open('backup.conf', 'r') as file:
            lines = file.readlines()
        lines[0] = 'Directory = ' + data_file + '\n'
        with open('backup.conf', 'w') as file:
            file.writelines(lines)
        messagebox.showinfo('Успешно.', 'Сохранено ' + data_file)
    elif '/' not in data_file:
        messagebox.showerror('Ошибка.', 'Неверный путь ' + data_file)
    else:
        with open('backup.conf', 'r') as file:
            lines = file.readlines()
        lines[0] = 'Directory = ' + data_file + '\n'
        with open('backup.conf', 'w') as file:
            file.writelines(lines)
        messagebox.showinfo('Успешно.', 'Сохранено ' + data_file)

src = os.path.realpath('./dist/backup.exe')
dst = os.path.realpath('./backup.exe')

root = tkinter.Tk()
root.geometry('660x380')
if sys.platform == 'win32':
    root.iconbitmap(default='backup.ico')
root.title('File backup settings ver 0.1b')
label_registry_entry = tkinter.Label(root, text='Упаковать в EXE?\n(возможно, потребуется установить дополнительные пакеты)')
data_dir_label = tkinter.Label(root, text='Введите полный путь до файла, который нужно копировать:')
email_label = tkinter.Label(root, text='Отправка письма на электроную почту в случае неудачного бекапа\n'
                            '(если сохранить пустые e-mail, функция будет отключена)')
data_my_email_label = tkinter.Label(root, text='Введите адрес e-mail, с которого отправлять:')
data_password_label = tkinter.Label(root, text='Введите пароль:')
data_you_email_label = tkinter.Label(root, text='Введите адрес e-mail, на который отправлять:')
data_smtp_label = tkinter.Label(root, text='Введите сервер smtp и порт, на котором находиться \nваша почта:'
                                '(по умолчанию сервер smtp.gmail.com и порт 587)')
data_dir = tkinter.Entry(root, bd='2', width='80')
data_my_email = tkinter.Entry(root, bd='2', width='50')
data_you_email = tkinter.Entry(root, bd='2', width='50')
data_password = tkinter.Entry(root, bd='2', width='50', show='*')
data_serv_smtp = tkinter.Entry(root, bd='2', width='40')
data_port_smtp = tkinter.Entry(root, bd='2', width='7')
delete_data_email = tkinter.Button(root, text='Очистить', command=delete_data_email)
save_email = tkinter.Button(root, text='Сохранить e-mail', command=save_email)
packing_exe = tkinter.Button(root, text='Упаковать в EXE', command=packing_exe)
review = tkinter.Button(root, text='Обзор', command=review)
save = tkinter.Button(root, text='Сохранить путь', command=save)
quit_not_save = tkinter.Button(root, text='Выйти', command=root.destroy)
label_registry_entry.place(x=150, y=10)
packing_exe.place(x=270, y=50)
email_label.place(x=140, y=80)
delete_data_email.place(x=420, y=167)
save_email.place(x=405, y=223)
data_my_email_label.place(x=70, y=110)
data_my_email.place(x=71, y=130)
data_password_label.place(x=70, y=150)
data_password.place(x=71, y=170)
data_smtp_label.place(x=70, y=190)
data_serv_smtp.place(x=71, y=225)
data_port_smtp.place(x=330, y=225)
data_you_email_label.place(x=70, y=245)
data_you_email.place(x=71, y=265)
review.place(x=570, y=313)
data_dir_label.place(x=175, y=290)
data_dir.place(x=70, y=315)
save.place(x=150, y=343)
quit_not_save.place(x=430, y=343)

tkinter.mainloop()
