import math

MAX_VALUE = 10000

#Проверяет коэффициенты что не превышают допустимый модуль дает ошибку если какой-то коэффициент вне диапазона
def check_coefficients(a, b, c): 
    if abs(a) > MAX_VALUE:
        raise ValueError("Ошибка: коэффициент A вне допустимого диапазона")
    if abs(b) > MAX_VALUE:
        raise ValueError("Ошибка: коэффициент B вне допустимого диапазона")
    if abs(c) > MAX_VALUE:
        raise ValueError("Ошибка: коэффициент C вне допустимого диапазона")

#Решает уравнение. дает ошибку при недопустимых коэффициентах
def solve(a, b, c):
    #проверяем данные
    check_coefficients(a, b, c)

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