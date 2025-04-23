# hexlet_code/differ.py
import json

def load_data(filepath):
    """Загружает данные из JSON-файла. В случае ошибки выбрасывает исключение."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    # Для библиотеки лучше выбрасывать исключения, а не печатать и выходить
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{filepath}'")
    except json.JSONDecodeError:
        # Указываем имя файла в сообщении об ошибке JSON
        raise json.JSONDecodeError(f"Invalid JSON in file: '{filepath}'", "", 0)
    except Exception as e:
        # Перевыбрасываем другие ошибки, сохраняя контекст
        raise Exception(f"Error reading file '{filepath}': {e}") from e

def to_string(value):
    """Конвертирует значение Python в строку для вывода diff."""
    if isinstance(value, bool):
        return str(value).lower()  # True -> 'true', False -> 'false'
    if value is None:
        return 'null'  # None -> 'null'
    # Остальные типы (числа, строки) конвертируем как есть
    return str(value)

def generate_diff(file_path1, file_path2):
    """
    Сравнивает два JSON-файла и возвращает строку с различиями
    в заданном формате.
    """
    # Загружаем данные из файлов
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)

    # Получаем все уникальные ключи из обоих словарей, сортируем по алфавиту
    keys = sorted(list(set(data1.keys()) | set(data2.keys())))

    diff_lines = []
    for key in keys:
        value1 = data1.get(key)  # Используем get для безопасного доступа
        value2 = data2.get(key)

        # Преобразуем значения в строки для вывода
        str_value1 = to_string(value1)
        str_value2 = to_string(value2)

        if key not in data2:
            # Ключ есть только в первом файле (удален)
            diff_lines.append(f"  - {key}: {str_value1}")
        elif key not in data1:
            # Ключ есть только во втором файле (добавлен)
            diff_lines.append(f"  + {key}: {str_value2}")
        elif value1 == value2:
            # Ключ есть в обоих, значения совпадают (не изменен)
            diff_lines.append(f"    {key}: {str_value1}")
        else:
            # Ключ есть в обоих, значения разные (изменен)
            diff_lines.append(f"  - {key}: {str_value1}")
            diff_lines.append(f"  + {key}: {str_value2}")

    # Собираем финальную строку вывода
    result = "{\n" + "\n".join(diff_lines) + "\n}"
    return result
