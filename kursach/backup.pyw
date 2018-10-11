import sys, os, shutil, threading, time, tkinter, platform, smtplib, logging
from datetime import datetime, timedelta
from tkinter import ttk
from tkinter import messagebox
from email.mime.text import MIMEText

# Проверка файла backup.conf
def cfg_verification():
    backup_txt = 'Directory =\nMy_email =\nPassword = \nServer SMTP = smtp.gmail.com\nPort SMTP = 587\nYou_email =\n'
    try:
        file = open(os.path.realpath('./backup.conf'))
        file.close()
    except:
        with open(os.path.realpath('./backup.conf'), 'w') as file:
            file.writelines(backup_txt)


# Отправка письма в случае неудачи
def smtp():
    with open('backup.conf', 'r') as file:
        lines = file.readlines()
    dir_my = lines[1].rsplit('=', 2)
    dir_pass = lines[2].rsplit('=', 2)
    dir_serv = lines[3].rsplit('=', 2)
    dir_port = lines[4].rsplit('=', 2)
    dir_you = lines[5].rsplit('=', 2)
    tmp_my = dir_my[1]
    tmp_pass = dir_pass[1]
    tmp_serv = dir_serv[1]
    tmp_port = dir_port[1]
    tmp_you = dir_you[1]
    fp = 'Бекап завершился неудачно на компьютере с именем ' + myhost
    msg = MIMEText(fp)
    serv_smtp = tmp_serv[1:-1]
    port_smtp = tmp_port[1:-1]
    my = tmp_my[1:-1]
    password = tmp_pass[1:-1]
    you = tmp_you[1:-1]
    msg['Subject'] = 'Бекап завершился неудачно!'
    msg['From'] = my
    msg['To'] = you
    if my == '':
        return
    if you == '':
        return
    s = smtplib.SMTP(serv_smtp, port_smtp)
    s.starttls()
    s.login(my, password)
    s.sendmail(my, you, msg.as_string())
    s.quit()

# Функция проверки, запускался ли скрипт сегодня?
def check_start():
    global flag
    root = tkinter.Tk()
    root.withdraw()
    for key in files_daily:
        base_daily = os.path.splitext(key)[0]
        if now.strftime('%d.%m.%Y') == base_daily:
            messagebox.showinfo('Внимание!', 'Бекап уже выполнялся сегодня')
            logging.warning('Бекап уже выполнялся сегодня.')
            flag += 4
            sys.exit()
    for key in files_weekly:
        base_weekly = os.path.splitext(key)[0]
        if now.strftime('%d.%m.%Y') == base_weekly:
            messagebox.showinfo('Внимание!', 'Бекап уже выполнялся сегодня')
            logging.warning('Бекап уже выполнялся сегодня.')
            flag += 4
            sys.exit()
    for key in files_monthly:
        base_monthly = os.path.splitext(key)[0]
        if now.strftime('%d.%m.%Y') == base_monthly:
            messagebox.showinfo('Внимание!', 'Бекап уже выполнялся сегодня')
            logging.warning('Бекап уже выполнялся сегодня.')
            flag += 4
            sys.exit()
    for key in files_yearly:
        base_yearly = os.path.splitext(key)[0]
        if now.strftime('%d.%m.%Y') == base_yearly:
            messagebox.showinfo('Внимание!', 'Бекап уже выполнялся сегодня')
            logging.warning('Бекап уже выполнялся сегодня.')
            flag += 4
            sys.exit()

# Функция проверки, существуют ли нужные нам папки, если нет, то создаем их
def check_dir():
    if not os.path.exists(dir_daily):
        os.makedirs(dir_daily)
    if not os.path.exists(dir_weekly):
        os.makedirs(dir_weekly)
    if not os.path.exists(dir_monthly):
        os.makedirs(dir_monthly)
    if not os.path.exists(dir_yearly):
        os.makedirs(dir_yearly)
    if not os.path.exists(dir_tmp):
        os.makedirs(dir_tmp)

# Функция сортировки по папкам
def sort_in_folders():
    if ref_day_month == now.strftime('%d.%m'):
        shutil.move(dir_tmp_file, dir_yearly)
    elif ref_day == now_day:
        shutil.move(dir_tmp_file, dir_monthly)
    elif ref_day == day_week:
        shutil.move(dir_tmp_file, dir_weekly)
    else:
        shutil.move(dir_tmp_file, dir_daily)

# Функция удаления неактуальных бекапов
def clean_backup():
    for key in files_daily:
        base_daily = os.path.splitext(key)[0]
        base_date_daily = datetime.strptime(base_daily, '%d.%m.%Y')
        base_end_date_daily = base_date_daily + timedelta(days=days)
        if now > base_end_date_daily:
            os.remove(dir_daily + key)
    for key in files_weekly:
        base_weekly = os.path.splitext(key)[0]
        base_date_weekly = datetime.strptime(base_weekly, '%d.%m.%Y')
        base_end_date_weekly = base_date_weekly + timedelta(weeks=weeks)
        if now > base_end_date_weekly:
            os.remove(dir_weekly + key)
    for key in files_monthly:
        base_monthly = os.path.splitext(key)[0]
        base_date_monthly = datetime.strptime(base_monthly, '%d.%m.%Y')
        base_end_date_monthly = base_date_monthly + timedelta(days=months)
        if now > base_end_date_monthly:
            os.remove(dir_monthly + key)
    for key in files_yearly:
        base_yearly = os.path.splitext(key)[0]
        base_date_yearly = datetime.strptime(base_yearly, '%d.%m.%Y')
        base_end_date_yearly = base_date_yearly + timedelta(days=years)
        if now > base_end_date_yearly:
            os.remove(dir_yearly + key)

#  Функция кнопки "Прервать"
def quit_bar():
    global flag
    flag += 4
    sys.exit()

# Первый поток - прогрессбар таймер выполнения
def thread_progressbar(a):
    # Таймер выполнения
    def timer_min():
        global min
        if sec == 0:
            min += 1
        time_min['text'] = 'Время выполнения: {} м.'.format(min)
        time_sec.after(1000, timer_min)
    def timer_sec():
        global sec
        if flag == 5:
            pass
        else:
            sec += 1
        time_sec['text'] = '{} с.'.format(sec)
        if sec == 59:
            sec = -1
        time_sec.after(1000, timer_sec)
    # Прогрессбар
    def run():
        global flag
        progress_bar['maximum'] = a
        for key in range(250):
            if flag == 1:
                time.sleep(0.01)
                progress_bar['value'] = key
                progress_bar.update()
            elif flag == 4:
                sys.exit()
            else:
                time.sleep(0.2)
                progress_bar['value'] = key
                progress_bar.update()
        label_progressbar.config(text='Архивирование файла...')
        for key in range(250, 500):
            if flag == 2:
                time.sleep(0.01)
                progress_bar['value'] = key
                progress_bar.update()
            elif flag == 5:
                os.system('taskkill /im 7za.exe /f > nul')
                sys.exit()
            else:
                time.sleep(0.5)
                progress_bar['value'] = key
                progress_bar.update()
        label_progressbar.config(text='Чистка мусора...')
        for key in range(500, 750):
            if flag == 3:
                time.sleep(0.01)
                progress_bar['value'] = key
                progress_bar.update()
            elif flag == 6:
                sys.exit()
            else:
                time.sleep(0.1)
                progress_bar['value'] = key
                progress_bar.update()
        label_progressbar.config(text='Завершение...')
        for key in range(750, 1001):
            time.sleep(0.001)
            progress_bar['value'] = key
            progress_bar.update()
        time.sleep(1)
        flag = 5
        label_progressbar.config(text='Завершено.')
        quit.config(text='Выйти')
    root = tkinter.Tk()
    root.geometry('522x100')
    if sys.platform == 'win32':
        root.iconbitmap(default='backup.ico')
    root.title('File backup ver 0.1b')
    label_progressbar = tkinter.Label(root, text='Копирование файла...')
    time_min = tkinter.Label(root)
    time_sec = tkinter.Label(root)
    progress_bar = ttk.Progressbar(root, orient='horizontal', length=500, mode='determinate')
    quit = tkinter.Button(root, width=10, text='Прервать', command=quit_bar)
    label_progressbar.place(x=10, y=10)
    time_min.place(x=364, y=10)
    time_sec.place(x=488, y=10)
    progress_bar.place(x=10, y=40)
    quit.place(x=440, y=70)
    root.eval('tk::PlaceWindow %s' % root.winfo_pathname(root.winfo_id()))
    timer_sec()
    timer_min()
    run()
    root.mainloop()

# Второй поток - бекап
def thread_backup():
    global flag

    # Попытка копирования
    try:
        shutil.copy2(src, dst)
        flag += 1
        logging.info('Копирование прошло успешно.')
    except(FileNotFoundError):
        smtp()
        flag += 4
        logging.exception('')
        logging.error('Не удалось найти указанный файл.')
        sys.exit()
    except:
        smtp()
        flag += 4
        logging.exception('')
        logging.error('Бекап выполнился неудачно. Ошибка неизвестна.')
        sys.exit()

    # Попытка архивирование бекапа
    try:
        os.system(archive)
        flag += 1
        logging.info('Архивирование прошло успешно.')
        time.sleep(3)
    except(FileNotFoundError):
        smtp()
        flag += 4
        logging.exception('')
        logging.error('Архивирование прошло неудачно. Не найден указанный файл.')
        sys.exit()
    except:
        smtp()
        flag += 4
        logging.exception('')
        logging.error('Архивирование прошло неудачно. Ошибка неизвестна.')
        sys.exit()

    try:
        os.remove(remove_file)
        sort_in_folders()
        logging.info('Сортировка прошла успешно.')
    except:
        logging.exception('')
        logging.error('Сортировка прошла неудачно. Ошибка неизвестна.')
        sys.exit()
    try:
        clean_backup()
        logging.info('Чистка мусора прошла успешно.')
        flag += 1
    except:
        logging.exception('')
        logging.error('Чистка мусора прошла неудачно. Ошибка неизвестна.')
        sys.exit()
    close(backup.log)

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename='backup.log')

cfg_verification()
with open('backup.conf', 'r') as file:
    lines = file.readlines()
dir = lines[0].rsplit('=', 2)
tmp_src = dir[1]
src = tmp_src[1:-1]
if src == '':
    root = tkinter.Tk()
    root.withdraw()
    if messagebox.askyesno('Ошибка!', 'Пустой путь до файла. Зайти в settings.py и настроить бекап?'):
        import settings
    else:
        logging.error('Пустой путь до файла.')
    exit()
basename = os.path.basename(src)
sec = -1  # Переменная секунд таймера
min = -1  # Переменная минут таймера
myhost = platform.node()  # Имя компа
flag = 0  # Переменная-флаг для синхронизации потоков
ref_day = 1  # День сравнения
ref_day_month = '01.01'  # День и месяц сравнения
days = 7  # Количество дней для хранения ежедневных бекапов
weeks = 4  # Количество недель для хранения еженедельных бекапов
months = 26  # Количество недель для хранения ежемесячных бекапов
years = 260  # Количество недель для хранения ежегодных бекапов
now = datetime.now()  # Сегодняшняя дата
now_day = datetime.now().day  # Сегодняшний день
day_week = datetime.today().isoweekday()  # День недели в цифровом виде
if sys.platform == 'win32':
    dir_daily = os.path.realpath('./backup/daily/') + '\\'  # Папка для хранение ежедневных выгрузок
    dir_weekly = os.path.realpath('./backup/weekly/') + '\\'  # Папка для хранение еженедельных выгрузок
    dir_monthly = os.path.realpath('./backup/monthly/') + '\\'  # Папка для хранение ежемесячных выгрузок
    dir_yearly = os.path.realpath('./backup/yearly/') + '\\'  # Папка для хранение ежегодичных выгрузок
    dir_tmp = os.path.realpath('./backup/tmp/') + '\\'  # Папка временного хранения
    dir_tmp_file = dir_tmp + now.strftime('%d.%m.%Y') + '.7z'  # Папка временного хранения + файл
    dst = dir_tmp + basename  # Путь до временного хранения бекапа
    archive = '7za.exe a -mx1 ' + os.path.realpath('./backup/tmp/') + '\\' + now.strftime(
        '%d.%m.%Y') + '.7z ' + os.path.realpath('./backup/tmp/') + '\\' + basename + ' > nul'
        # Выполнение архивации в 7zip через командную строку
    remove_file = dir_tmp + basename  # Путь до не нужного файла
else:
    dir_daily = os.path.realpath('./backup/daily/')
    dir_weekly = os.path.realpath('./backup/weekly/')
    dir_monthly = os.path.realpath('./backup/monthly/')
    dir_yearly = os.path.realpath('./backup/yearly/')
    dir_tmp = os.path.realpath('./backup/tmp/')
    dir_tmp_file = dir_tmp + now.strftime('%d.%m.%Y') + '.7z'
    dst = dir_tmp + basename
    archive = '7z a -mx1 /backup/tmp/' + now.strftime(
        '%d.%m.%Y') + '.7z /backup/tmp/' + basename
    remove_file = dir_tmp + basename
progressbar = threading.Thread(target=thread_progressbar, name='progressbar', args=(1000,))
backup = threading.Thread(target=thread_backup, name='backup', daemon=True, args=())

if __name__ == '__main__':
    try:
        check_dir()
        logging.info('Проверка директорий прошла успешно.')
    except(SystemExit):
        pass
    except:
        logging.exception('')
        logging.error('Проверка директорий прошла неудачно. Ошибка неизвестна.')
        sys.exit()
    files_daily = os.listdir(dir_daily)
    files_weekly = os.listdir(dir_weekly)
    files_monthly = os.listdir(dir_monthly)
    files_yearly = os.listdir(dir_yearly)
    try:
        check_start()
        logging.info('Проверка запуска прошла успешно.')
    except(SystemExit):
        pass
    except:
        logging.exception('')
        logging.error('Проверка запуска прошла неудачно. Ошибка неизвестна.')
        sys.exit()

    progressbar.start()
    backup.start()
    progressbar.join()
