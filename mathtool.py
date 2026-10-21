import sys
from calc import equation

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

if len(args) == 0 or args[0] == '--help': 
    print(text_help) 
    sys.exit(0) 
        
elif args[0] == 'solve':
    # вариант 1: пользователь ввел только solve, запрашиваем числа поочередно
    if len(args) == 1:
        try: 
            A = int(input('Введите A: '))
        except ValueError: 
            print('Ошибка: это не число', file=sys.stderr)
            sys.exit(1)
        try: 
            B = int(input('Введите B: '))
        except ValueError: 
            print('Ошибка: это не число', file=sys.stderr)
            sys.exit(1)
        try: 
            C = int(input('Введите C: '))
        except ValueError: 
            print('Ошибка: это не число', file=sys.stderr)
            sys.exit(1)
        
    # вариант 2: пользователь ввел solve с аргументами
    elif len(args) == 7 and args[1] == '-a' and args[3] == '-b' and args[5] == '-c':
        A = args[2]
        B = args[4]
        C = args[6]
    else:
        print('Ошибка: неверный набор параметров', file=sys.stderr)
        sys.exit(1)
else:
    print('Ошибка: неизвестная команда', file=sys.stderr)
    sys.exit(1)

# переводим в числа
try:  
    a = int(A)
    b = int(B)
    c = int(C)
except ValueError:
    print('Ошибка: заданный аргумент не является числом', file=sys.stderr)
    sys.exit(1)

# вызываем расчётную часть и обрабатываем её ошибки
try:
    kind, d, roots = equation.solve(a, b, c)
except ValueError as e:
    print(str(e), file=sys.stderr)
    sys.exit(1)

# выводим результат
if kind == "линейное":
    print('Линейное')
    print(f"x = {roots[0]:.3f}")
else:
    print('Квадратное')
    print('D =', d)

    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print('Действительных корней нет')