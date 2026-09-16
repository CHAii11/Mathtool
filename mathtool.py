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

