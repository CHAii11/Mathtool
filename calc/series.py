import math

# ограничения для команды series
MAX_TERMS = 10000          # максимум слагаемых
MAX_EPS = 0.0001           # самая грубая допустимая точность
MAX_ITERATIONS = 100000    # предел цикла по точности

# число знаков после запятой в выводе (из MAX_EPS)
DIGITS = math.ceil(-math.log10(MAX_EPS))


def sign(n): #Знак слагаемого: нечётные плюс, чётные минус
    if n % 2 == 0:
        return -1
    return 1


def term_sqplus(n): #Слагаемое ряда sqplus: знак(n) / (n в кв + 1)
    return sign(n) / (n * n + 1)


def term_third(n): #Слагаемое ряда third: знак(n) / (3 * n)
    return sign(n) / (3 * n)


# таблица рядов: ключ имя, значение (функция слагаемого, формула для вывода)
FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third":  (term_third,  "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
}


def sum_by_terms(term_func, count): #Сумма ряда по количеству слагаемых
    result = 0
    for n in range(1, count + 1):
        result += term_func(n)
    return result


def sum_by_eps(term_func, eps): #Сумма ряда по точности. Возвращает кортеж (сумма, количество слагаемых). ValueError, если точность не достигнута за MAX_ITERATIONS шагов
    result = 0
    for n in range(1, MAX_ITERATIONS + 1):
        value = term_func(n)
        result += value
        if abs(value) < eps:
            return result, n
    raise ValueError("точность не достигнута")