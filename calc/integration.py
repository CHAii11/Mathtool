#Интегрирование. Вместо того чтобы прибавлять шаг к предыдущему значению x = x + dx, каждый раз высчитываем её заново с нуля: берем начало отрезка a и прибавляем к нему номер шага i, 
#умноженный на ширину прямоугольника dx. Это спасает от накопления мелких погрешностей округления float, из-за которых программа могла бы сделать лишний шаг.

import math
# ограничения для команды integrate
MAX_STEPS = 100000
# число знаков после запятой в выводе
DIGITS = 4

def func_ratio(x): #Функция ratio: x / (x^2 + 1)
    return x / (x + 1)


def func_root(x): #Функция root: sqrt(x)
    return math.sqrt(x * x + 1)


#таблица функций: ключ имя, значение функция
FUNCTIONS = {
    "ratio": func_ratio,
    "root": func_root,}

#Метод левых прямоугольников: Нарезает график функции на steps кусочков
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