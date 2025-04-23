# hexlet_code/scripts/gendiff.py
import argparse
import sys

# Импортируем нашу основную библиотечную функцию
from hexlet_code import generate_diff

def main():
    # 1. Парсинг аргументов командной строки (остается как было)
    parser = argparse.ArgumentParser(
        description=(
            'Compares two configuration files and shows a difference.'
        )
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output'
        # Пока не используем args.format, но он нужен для следующих шагов
    )
    args = parser.parse_args()

    # 2. Вызов основной функции библиотеки и вывод результата
    try:
        # Передаем пути к файлам в функцию generate_diff
        diff_output = generate_diff(args.first_file, args.second_file)
        # Печатаем результат, который вернула функция
        print(diff_output)
    except FileNotFoundError as e:
        # Ловим и обрабатываем ошибки, выброшенные generate_diff/load_data
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Ловим другие возможные ошибки (например, JSONDecodeError)
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

# Стандартная конструкция Python
if __name__ == '__main__':
    main()
