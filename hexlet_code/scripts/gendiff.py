# hexlet_code/scripts/gendiff.py
import argparse

# Добавляем импорты для типов исключений парсеров
import json
import sys

import yaml

from hexlet_code import generate_diff


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
        help='set format of output'
    )
    args = parser.parse_args()

    try:
        diff_output = generate_diff(args.first_file, args.second_file)
        print(diff_output)
    # Обновляем блок except, чтобы ловить ошибки парсеров и ValueError
    except (FileNotFoundError, ValueError,
            json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Ловим остальные непредвиденные ошибки
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
