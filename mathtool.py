import sys
import math
MAX_VALUE = 10000
text_help = (
        "mathtool — решение уравнений вида A*x^2 + B*x + C = 0\n"
        "Использование:\n"
        "    python mathtool.py                         вывод справки\n"
        "    python mathtool.py --help                  вывод справки\n"
        "    python mathtool.py solve                   ввод коэффициентов с клавиатуры\n"
        "    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами\n"
        "Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000."
    )
args = sys.argv[1:] 


if len(args) == 0:
    print(text_help)  #cразу выводим справку
    
user_input = input('Введите команду: ')
user = user_input.split()
    
if len(user) == 0:
    print('Вы ничего не ввели', file=sys.stderr)
    sys.exit(1)
        
if user[0] == '--help':
    print(text_help)
    sys.exit(0)
        
elif user[0] == 'solve':
        #вариант 1 пользователь ввел только solve, то запрашиваем числа поочередно
        if len(user) == 1:
            try: 
                A = int(input('Введите A: '))
            except ValueError: 
                print('Ошибка: это не число', file=sys.stderr); sys.exit(1)
            try: 
                B = int(input('Введите B: '))
            except ValueError: 
                print('Ошибка: это не число', file=sys.stderr); sys.exit(1)
            try: 
                C = int(input('Введите C: '))
            except ValueError: 
                print('Ошибка: это не число', file=sys.stderr); sys.exit(1)
            
        #вариант 2 пользователь ввел solve с аргументами
        elif len(user) == 7 and user[1] == '-a' and user[3] == '-b' and user[5] == '-c':
            A = user[2]
            B = user[4]
            C = user[6]
        else:
            print('Ошибка: неверный набор параметров', file=sys.stderr)
            sys.exit(1)
else:
        print('Ошибка: неизвестная команда', file=sys.stderr)
        sys.exit(1)

try:  #переводим в числа
    a = int(A)
    b = int(B)
    c = int(C)
except ValueError:
    print('Ошибка: заданный аргумент не является числом', file=sys.stderr)
    sys.exit(1)

if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:  #проверка
     print('Ошибка: число вне допустимого диапазона', file=sys.stderr)
     sys.exit(1)

if a == 0:
    if b != 0:
        print('Линейное')
        x = -c / b
        print(f"x = {x:.3f}")
    else:
        print('Ошибка: это не уравнение', file=sys.stderr)
        sys.exit(1)
else:
    print('Квадратное')
    d = b * b - 4 * a * c
    print('D =', d)

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")

    elif d == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    else:
        print('Действительных корней нет')