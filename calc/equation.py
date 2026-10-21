import math

MAX_VALUE = 10000

#Проверяет коэффициенты дает ошибку если какой-то коэффициент вне диапазона
def check_coefficients(coefficients):
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"Ошибка: коэффициент {name} вне допустимого диапазона")

#Решает уравнение. дает ошибку при недопустимых коэффициентах
def solve(a, b, c):
    #проверяем данные
    check_coefficients({"A": a, "B": b, "C": c})

    #линейное уравнение
    if a == 0:
        if b == 0:
            raise ValueError("Ошибка: это не уравнение")
        x = -c / b
        return "линейное", None, [x]

    #квадратное уравнение
    d = b * b - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "квадратное", d, [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
        return "квадратное", d, [x]
    else:
        return "квадратное", d, []