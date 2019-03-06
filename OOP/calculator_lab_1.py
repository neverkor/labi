# Основной бесконечный цикл
while True:

    # Получаем данные которые вводит пользователь
    a = float(input('Введите первый операнд: '))
    b = float(input('Введите второй операнд: '))
    operation = int(input('1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n'
                          'Выберите действие, введя соответствующую цифру: '))

    # Условие выбора математического действия
    if operation == 1:
        c = a + b
        print(c)

        # Второй бесконечный цикл для продолжения работы, ввод новых чисел или выхода
        while True:

            # Получаем данные которые вводит пользователь
            proceed = int(input('1. Продолжить работу над результатом\n2. Ввод новый операндов\n3. Выход\n'
                              'Выберите действие, введя соответствующую цифру: '))

            # Условие выбора действия
            if proceed == 1:
                b = float(input('Введите второй операнд: '))
                operation = int(input('1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n'
                                      'Выберите действие, введя соответствующую цифру: '))

                # Условие выбора математического действия
                if operation == 1:
                    c = c + b
                    print(c)
                    continue
                elif operation == 2:
                    c = c - b
                    print(c)
                    continue
                elif operation == 3:
                    c = c * b
                    print(c)
                    continue
                elif operation == 4:
                    try:
                        c = c / b
                        print(c)
                    except(ZeroDivisionError):
                        print('На ноль делить нельзя! Повторите ввод')
                        continue
                else:
                    print('Нет такого действия. Повторите')

            # Здесь, если человек ввел 2 ввести новые операнды, через break мы выходим из второго цикла и ниже через
            # continue попадаем в начало основного цикла
            elif proceed == 2:
                break

            # Здесь, если человек ввел 3 Выход, просто завершаем принудительно программу через exit()
            elif proceed == 3:
                exit()
            else:
                print('Нет такого действия. Повторите')
        continue

# Ниже все индентично как показано выше, простая копипаста с заменой математических знаков


    if operation == 2:
        c = a - b
        print(c)
        while True:
            proceed = int(input('1. Продолжить работу над результатом\n2. Ввод новый операндов\n3. Выход\n'
                              'Выберите действие, введя соответствующую цифру: '))
            if proceed == 1:
                b = float(input('Введите второй операнд: '))
                operation = int(input('1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n'
                                      'Выберите действие, введя соответствующую цифру: '))
                if operation == 1:
                    c = c + b
                    print(c)
                    continue
                elif operation == 2:
                    c = c - b
                    print(c)
                    continue
                elif operation == 3:
                    c = c * b
                    print(c)
                    continue
                elif operation == 4:
                    try:
                        c = c / b
                        print(c)
                    except(ZeroDivisionError):
                        print('На ноль делить нельзя! Повторите ввод')
                        continue
                else:
                    print('Нет такого действия. Повторите')
            elif proceed == 2:
                break
            elif proceed == 3:
                exit()
            else:
                print('Нет такого действия. Повторите')
        continue
    elif operation == 3:
        c = a * b
        print(c)
        while True:
            proceed = int(input('1. Продолжить работу над результатом\n2. Ввод новый операндов\n3. Выход\n'
                              'Выберите действие, введя соответствующую цифру: '))
            if proceed == 1:
                b = float(input('Введите второй операнд: '))
                operation = int(input('1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n'
                                      'Выберите действие, введя соответствующую цифру: '))
                if operation == 1:
                    c = c + b
                    print(c)
                    continue
                elif operation == 2:
                    c = c - b
                    print(c)
                    continue
                elif operation == 3:
                    c = c * b
                    print(c)
                    continue
                elif operation == 4:
                    try:
                        c = c / b
                        print(c)
                    except(ZeroDivisionError):
                        print('На ноль делить нельзя! Повторите ввод')
                        continue
                else:
                    print('Нет такого действия. Повторите')
            elif proceed == 2:
                break
            elif proceed == 3:
                exit()
            else:
                print('Нет такого действия. Повторите')
        continue
    elif operation == 4:
        try:
            c = a / b
            print(c)
        except(ZeroDivisionError):
            print('На ноль делить нельзя! Повторите ввод')
            continue
        while True:
            proceed = int(input('1. Продолжить работу над результатом\n2. Ввод новый операндов\n3. Выход\n'
                                'Выберите действие, введя соответствующую цифру: '))
            if proceed == 1:
                b = float(input('Введите второй операнд: '))
                operation = int(input('1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n'
                                      'Выберите действие, введя соответствующую цифру: '))
                if operation == 1:
                    c = c + b
                    print(c)
                    continue
                elif operation == 2:
                    c = c - b
                    print(c)
                    continue
                elif operation == 3:
                    c = c * b
                    print(c)
                    continue
                elif operation == 4:
                    try:
                        c = c / b
                        print(c)
                    except(ZeroDivisionError):
                        print('На ноль делить нельзя! Повторите ввод')
                        continue
                else:
                    print('Нет такого действия. Повторите')
            elif proceed == 2:
                break
            elif proceed == 3:
                exit()
            else:
                print('Нет такого действия. Повторите')
        continue
    else:
        print('Нет такого действия')
        proceed = input('Начать заново? y/n: ')
        if proceed == 'n':
            break
