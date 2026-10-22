#Статистика вычисляет 11 показателей для набора чисел
import math
import sys

# ограничения для команды stats
MAX_COUNT = 20
MAX_ABS = 10000


def read_numbers(path): #Читает числа из файла или ввода. path - путь к файлу,или None для чтения из stdin. Возвращает список чисел. ValueError или OSError при ошибках
    # выбираем источник
    if path is not None:
        source = open(path, encoding="utf-8-sig")
    else:
        source = sys.stdin
    
    try:
        numbers = []
        for line in source:
            for word in line.split():
                try:
                    value = float(word)
                except ValueError:
                    raise ValueError(f"{word} не является числом")
                
                # проверяем конечность
                if not math.isfinite(value):
                    raise ValueError(f"{word} не является конечным числом")
                
                # проверяем диапазон
                if abs(value) > MAX_ABS:
                    raise ValueError(f"значение {value} вне допустимого диапазона")
                
                numbers.append(value)
    finally:
        # закрываем файл, если открывали
        if path is not None:
            source.close()
    
    # проверяем количество
    if len(numbers) == 0:
        raise ValueError("последовательность пуста")
    if len(numbers) > MAX_COUNT:
        raise ValueError(f"слишком много чисел: {len(numbers)} (максимум {MAX_COUNT})")
    
    return numbers


#функции показателей
def count(values): #Количество чисел
    return len(values)

def total(values): #Сумма чисел
    result = 0
    for v in values:
        result += v
    return result

def mean(values): #Среднее арифметическое
    return total(values) / len(values)

def sum_of_squares(values): #Сумма квадратов
    result = 0
    for v in values:
        result += v ** 2
    return result

def rms(values): #Среднее квадратическое
    return math.sqrt(sum_of_squares(values) / len(values))

def sum_of_squared_deviations(values): #Сумма квадратов отклонений от среднего
    m = mean(values)
    result = 0
    for v in values:
        result += (v - m) ** 2
    return result

def variance(values): #Дисперсия по N
    return sum_of_squared_deviations(values) / len(values)

def std_dev(values): #СКО корень из дисперсии, по N
    return math.sqrt(variance(values))

def sample_std_dev(values): #Стандартное отклонение по N-1. Не существует при одном числе
    if len(values) < 2:
        return None
    return math.sqrt(sum_of_squared_deviations(values) / (len(values) - 1))

def minimum(values): #Наименьшее значение
    result = values[0]
    for v in values:
        if v < result:
            result = v
    return result

def maximum(values): #Наибольшее значение
    result = values[0]
    for v in values:
        if v > result:
            result = v
    return result

def positive_count(values): #Количество положительных чисел
    result = 0
    for v in values:
        if v > 0:
            result += 1
    return result

def negative_count(values): #Количество отрицательных чисел
    result = 0
    for v in values:
        if v < 0:
            result += 1
    return result


#таблица показателей: подпись, функция, формат
REPORT = [
    ("Количество", count, "d"),
    ("Сумма", total, ".3f"),
    ("Ср. арифм.", mean, ".3f"),
    ("Сумма кв.", sum_of_squares, ".3f"),
    ("Ср. кв.", rms, ".3f"),
    ("Дисперсия", variance, ".3f"),
    ("СКО", std_dev, ".3f"),
    ("Станд. откл.", sample_std_dev, ".3f"),
    ("Наименьшее", minimum, ".3f"),
    ("Наибольшее", maximum, ".3f"),
    ("Положительных", positive_count, "d"),
    ("Отрицательных", negative_count, "d"),]