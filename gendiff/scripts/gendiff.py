# gendiff/scripts/gendiff.py
import argparse
import json

# Добавляем импорт OSError, т.к. теперь ловим его явно
import sys

import yaml

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
    # ИСПРАВЛЕНО: Добавляем OSError и убираем общий Exception
    except (FileNotFoundError, ValueError, OSError,
            json.JSONDecodeError, yaml.YAMLError) as e:
        # Обрабатываем все ожидаемые ошибки файлов, парсинга, формата
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    # Блок 'except Exception as e:' УДАЛЕН.
    # Неожиданные ошибки приведут к падению программы с трассировкой.


if __name__ == '__main__':
    main()
