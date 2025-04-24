# gendiff/scripts/gendiff.py
import argparse
import json
import sys

import yaml

# OSError импортировать не нужно, он встроенный
# import os # Этот импорт теперь не нужен здесь
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
    # ИСПРАВЛЕНО: Убираем FileNotFoundError, т.к. OSError его включает
    except (ValueError, OSError,  # <--- Убрали FileNotFoundError
            json.JSONDecodeError, yaml.YAMLError) as e:
        # Обрабатываем все ожидаемые ошибки файлов, парсинга, формата
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    # Блок 'except Exception as e:' был удален ранее


if __name__ == '__main__':
    main()
