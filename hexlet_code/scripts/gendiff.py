# hexlet_code/scripts/gendiff.py
import argparse
import json
import sys

import yaml  # Оставляем импорты для обработки исключений

from hexlet_code import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Указываем 'stylish' как значение по умолчанию для формата
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        default='stylish',  # <-- Значение по умолчанию
        help='set format of output (default: "stylish")'
    )
    args = parser.parse_args()

    try:
        # Передаем имя формата в generate_diff
        diff_output = generate_diff(
            args.first_file, args.second_file, format_name=args.format
        )
        print(diff_output)
    # Блок except остается прежним
    except (FileNotFoundError, ValueError,
            json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
