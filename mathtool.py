import sys
from calc import equation
from cli import build_parser
from calc import stats

def handle_solve(args): #Обработчик команды solve
    # проверяем: либо все три коэффициента, либо ни одного
    if args.a is not None or args.b is not None or args.c is not None:
        if args.a is None or args.b is None or args.c is None:
            raise ValueError("укажите все три коэффициента либо ни одного")
        a, b, c = args.a, args.b, args.c
    else:
        # ввод с клавиатуры
        try:
            a = int(input('Введите A: '))
            b = int(input('Введите B: '))
            c = int(input('Введите C: '))
        except ValueError:
            raise ValueError("коэффициент не является целым числом")
    
    # вызываем расчётную часть
    kind, d, roots = equation.solve(a, b, c)
    
    # выводим результат
    if kind == "линейное":
        print('Линейное')
        print(f"x = {roots[0]:.3f}")
    else:
        print('Квадратное')
        print('D =', d)
        if len(roots) == 2:
            print(f"x1 = {roots[0]:.3f}")
            print(f"x2 = {roots[1]:.3f}")
        elif len(roots) == 1:
            print(f"x = {roots[0]:.3f}")
        else:
            print('Действительных корней нет')
    
    return 0

def handle_stats(args): #Обработчик команды stats
    numbers = stats.read_numbers(args.input)
    
    for label, function, form in stats.REPORT:
        value = function(numbers)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")
    
    return 0

def main(argv): #Главная функция приложения. Возвращает код завершения
    parser = build_parser()
    args = parser.parse_args(argv)
    
    # Если команда не указана — выводим справку
    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return handle_solve(args)
        elif args.command == "stats":
            return handle_stats(args)

        else:
            print(f'Ошибка: команда {args.command} ещё не реализована', file=sys.stderr)
            return 1
    except (ValueError, OSError) as error:
        print(f'ОШИБКА: {error}', file=sys.stderr)
        return 1

# Точка входа
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))