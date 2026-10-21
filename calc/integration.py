import math
# ограничения для команды integrate
MAX_STEPS = 100000
# число знаков после запятой в выводе
DIGITS = 4

def func_ratio(x): #Функция ratio: x / (x^2 + 1)
    return x / (x * x + 1)


def func_root(x): #Функция root: sqrt(x)
    return math.sqrt(abs(x))


#таблица функций: ключ имя, значение функция
FUNCTIONS = {
    "ratio": func_ratio,
    "root": func_root,}

def integrate(func, start, end, steps): #Численное интегрирование методом левых прямоугольников. Возвращает значение интеграла. ValueError при недопустимых пределах
    if start > end:
        raise ValueError("нижний предел больше верхнего")
    
    if start == end:
        return 0.0
    
    h = (end - start) / steps
    result = 0
    for i in range(steps):
        x = start + i * h
        result += func(x)
    return result * h