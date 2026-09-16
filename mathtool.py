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


if len(args) == 0 or args[0] == '--help': #вывод справки во всех возможных случаях
    print(text_help)
    sys.exit(0)

if args[0] != 'solve': #если ввели не то что нужно 
    print('Ошибка: неизвестная команда', file=sys.stderr)
    sys.exit(1)

if len(args) == 1:  #если ввели только solve, просим числа
    try:
        A = int(input('Введите A:'))
    except ValueError:
        print('Ошибка: это не является числом',file=sys.stderr)
        sys.exit(1)
    try:
            B = int(input('Введите B:'))
    except ValueError:
        print('Ошибка: это не является числом',file=sys.stderr)
        sys.exit(1)
    try:
        C = int(input('Введите C:'))
    except ValueError:
        print('Ошибка: это не является числом', file=sys.stderr)
        sys.exit(1)
elif len(args) == 7 and args[1] == '-a' and args[3] == '-b' and args[5] == '-c': #запоминаем введенное 
    A = args[2]
    B = args[4]
    C = args[6]
else:
    print('Ошибка: неверный набор чисел', file=sys.stderr)
    sys.exit(1)

try:  #переводим в числа
    a = int(A)
    b = int(B)
    c = int(C)
except ValueError:
    print('Ошибка: заданный коэффициент не является числом', file=sys.stderr)
    sys.exit(1)

if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:  #проверка
     print('Ошибка: число вне допустимого диапазона', file=sys.stderr)
     sys.exit(1)
