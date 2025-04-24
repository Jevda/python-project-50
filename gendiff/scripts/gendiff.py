# gendiff/scripts/gendiff.py
import argparse
import sys

import yaml

# import os # Убрали как неиспользуемый
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
    # ИСПРАВЛЕНО: Убран комментарий в конце строки
    except (ValueError, OSError, yaml.YAMLError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
