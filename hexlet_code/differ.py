# hexlet_code/differ.py
# Убираем 'import json'
from .parsers import parse_data  # Импортируем новую функцию


# Функция to_string остается без изменений
def to_string(value):
    """Конвертирует значение Python в строку для вывода diff."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)

# Функция load_data УДАЛЕНА


def generate_diff(file_path1, file_path2):
    """
    Сравнивает два файла (JSON или YAML) и возвращает строку
    с различиями в заданном формате.
    """
    # Используем новую функцию parse_data
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    # Логика сравнения остается ТОЧНО ТАКОЙ ЖЕ
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
