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
print(text_help)
user_input = input("Введите команду и числа: ")
parts = user_input.split

if user_input == "--help":
    print(text_help)

if len(parts) == 1 and user_input == "solve":
   A = int(input("Введите А"))
   B = int(input("Введите B"))
   C = int(input("Введите C"))

if user_input != "solve" and user_input != "--help":
    print("Ошибка, неизвестная команда")
    