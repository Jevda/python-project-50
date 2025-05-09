# hexlet_code/parsers.py
import json
import os
import sys

import yaml


def get_file_extension(filepath):
    """Получает расширение файла в нижнем регистре."""
    _, extension = os.path.splitext(filepath)
    return extension.lower()


def parse_data(filepath):
    """
    Читает данные из файла и парсит их в зависимости от расширения.
    Поддерживает .json, .yml, .yaml.
    Возвращает словарь Python.
    Выбрасывает исключения при ошибках.
    """
    extension = get_file_extension(filepath)

    # Отладочная печать (можешь удалить, если больше не нужна)
    print(f"DEBUG: Attempting to open: [{filepath}]", file=sys.stderr)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            if extension == '.json':
                return json.load(f)
            elif extension == '.yml' or extension == '.yaml':
                return yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported file format: '{extension}'")
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{filepath}'")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON in file: '{filepath}'", e.doc, e.pos
        ) from e
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Invalid YAML in file: '{filepath}': {e}")
    except ValueError as e:
        raise e
    # ИСПРАВЛЕНО: Ловим более конкретную ошибку OSError
    except OSError as e:
        error_message = (
            f"An OS error occurred while reading file '{filepath}': {e}"
        )
        # Перевыбрасываем как OSError или можно обернуть в свое исключение,
        # но OSError тут вполне подходит.
        raise OSError(error_message) from e
    # Убираем перехват общего Exception, чтобы не скрывать неожиданные ошибки
