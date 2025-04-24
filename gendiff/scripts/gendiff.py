# gendiff/scripts/gendiff.py
import argparse
# Убираем неиспользуемый импорт json, т.к. исключение ловится через ValueError
# import json
import sys
# Импорт yaml нужен для yaml.YAMLError
import yaml
# Импорт os не нужен здесь (OSError встроенный)
# import os

# Импортируем из пакета gendiff
from gendiff import generate_diff


def main():
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
        default='stylish',
        help='set format of output (default: "stylish")'
    )
    args = parser.parse_args()

    try:
        diff_output = generate_diff(
            args.first_file, args.second_file, format_name=args.format
        )
        print(diff_output)
    # ИСПРАВЛЕНО: Убираем json.JSONDecodeError, т.к. ValueError его включает
    except (ValueError, OSError, yaml.YAMLError) as e: # <-- Убрали json.JSONDecodeError
        # Обрабатываем все ожидаемые ошибки файлов, парсинга, формата
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    # Неожиданные ошибки приведут к падению программы с трассировкой.


if __name__ == '__main__':
    main()
