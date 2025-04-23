# hexlet_code/differ.py
import json


def load_data(filepath):
    """
    Загружает данные из JSON-файла.
    В случае ошибки выбрасывает исключение.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{filepath}'")
    except json.JSONDecodeError:
        # Создаем сообщение об ошибке отдельно
        error_message = f"Invalid JSON in file: '{filepath}'"
        # Передаем его конструктору исключения
        raise json.JSONDecodeError(error_message, "", 0)
    except Exception as e:
        # Формируем сообщение и перевыбрасываем исключение
        error_message = (
            f"An error occurred while reading file '{filepath}': {e}"
        )
        raise Exception(error_message) from e


def to_string(value):
    """Конвертирует значение Python в строку для вывода diff."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def generate_diff(file_path1, file_path2):
    """
    Сравнивает два JSON-файла и возвращает строку с различиями
    в заданном формате.
    """
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)

    keys = sorted(list(set(data1.keys()) | set(data2.keys())))

    diff_lines = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        str_value1 = to_string(value1)
        str_value2 = to_string(value2)

        if key not in data2:
            diff_lines.append(f"  - {key}: {str_value1}")
        elif key not in data1:
            diff_lines.append(f"  + {key}: {str_value2}")
        elif value1 == value2:
            diff_lines.append(f"    {key}: {str_value1}")
        else:
            diff_lines.append(f"  - {key}: {str_value1}")
            diff_lines.append(f"  + {key}: {str_value2}")

    result = "{\n" + "\n".join(diff_lines) + "\n}"
    return result
