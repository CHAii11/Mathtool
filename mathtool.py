import sys
import math
MAX_VALUE = 10000
args_count = len(sys.argv) - 1
text_heip = (
        "mathtool — решение уравнений вида A*x^2 + B*x + C = 0\n"
        "Использование:\n"
        "    python mathtool.py                         вывод справки\n"
        "    python mathtool.py --help                  вывод справки\n"
        "    python mathtool.py solve                   ввод коэффициентов с клавиатуры\n"
        "    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами\n"
        "Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000."
    )
if args_count == 0 or sys.argv[1] == '--help':
    print(text_heip)
    sys.exit(0)
