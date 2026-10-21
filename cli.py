import argparse

def build_parser(): # Создаём главный разборщик
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — решение уравнений и обработка числовых рядов",
        allow_abbrev=False)  # запрещаем сокращения параметров
    
    # Создаём набор подкоманд
    subparsers = parser.add_subparsers(dest="command")
    
    # Команда solve
    solve_parser = subparsers.add_parser(
        "solve",
        help="решение уравнения A*x^2 + B*x + C = 0",
        allow_abbrev=False)
    solve_parser.add_argument("-a", type=int, help="коэффициент A (целое, |A| <= 10000)")
    solve_parser.add_argument("-b", type=int, help="коэффициент B (целое, |B| <= 10000)")
    solve_parser.add_argument("-c", type=int, help="коэффициент C (целое, |C| <= 10000)")
    
    # Команда stats
    stats_parser = subparsers.add_parser(
        "stats",
        help="показатели последовательности чисел",
        allow_abbrev=False)
    stats_parser.add_argument("--input", help="имя файла с числами (без него — стандартный ввод)")
    
    # Команда series
    series_parser = subparsers.add_parser(
        "series",
        help="сумма знакочередующегося ряда",
        allow_abbrev=False)
    series_parser.add_argument("--func", required=True, help="имя ряда (sqplus, third)")
    # Группа ровно один из --terms или --eps
    group = series_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="количество слагаемых (от 1 до 10000)")
    group.add_argument("--eps", type=float, help="точность (0 < eps <= 0.0001)")
    
    # Команда integrate
    integrate_parser = subparsers.add_parser(
        "integrate",
        help="численное интегрирование методом левых прямоугольников",
        allow_abbrev=False)
    integrate_parser.add_argument("--func", required=True, help="имя функции (ratio, root)")
    integrate_parser.add_argument("--from", dest="start", type=float, required=True,
                                  help="нижний предел интегрирования")
    integrate_parser.add_argument("--to", type=float, required=True,
                                  help="верхний предел интегрирования")
    integrate_parser.add_argument("--steps", type=int, required=True,
                                  help="число прямоугольников (от 1 до 100000)")
    
    return parser