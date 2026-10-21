import sys
from calc import equation
from cli import build_parser

def main(argv):
    """Главная функция приложения. Возвращает код завершения."""
    parser = build_parser()
    args = parser.parse_args(argv)
    
    # Если команда не указана — выводим справку
    if args.command is None:
        parser.print_help()
        return 0
    
    # Обработка команды solve
    if args.command == "solve":
        # Проверка: либо все три коэффициента, либо ни одного
        if args.a is not None or args.b is not None or args.c is not None:
            if args.a is None or args.b is None or args.c is None:
                print('Ошибка: укажите все три коэффициента либо ни одного', file=sys.stderr)
                return 1
            a, b, c = args.a, args.b, args.c
        else:
            # Ввод с клавиатуры
            try:
                a = int(input('Введите A: '))
                b = int(input('Введите B: '))
                c = int(input('Введите C: '))
            except ValueError:
                print('Ошибка: коэффициент не является целым числом', file=sys.stderr)
                return 1
    
        # вызываем расчётную часть и обрабатываем её ошибки
        try:
            kind, d, roots = equation.solve(a, b, c)
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 1
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
    
    # Пока другие команды не реализованы
    print(f'Ошибка: команда {args.command} ещё не реализована', file=sys.stderr)
    return 1

# Точка входа
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))