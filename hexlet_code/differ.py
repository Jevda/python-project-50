# hexlet_code/differ.py
# Импортируем построитель дерева
from .diff_builder import build_diff_tree

# Импортируем нужный форматер
from .formatters.stylish import format_stylish
from .parsers import parse_data

# Функция to_string больше не нужна здесь, ее логика ушла в format_value
# def to_string(value): ...


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Сравнивает два файла и возвращает строку с различиями
    в заданном формате ('stylish' по умолчанию).
    """
    # Шаг 1: Парсинг файлов
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    # Шаг 2: Построение внутреннего дерева различий
    diff_tree = build_diff_tree(data1, data2)

    # Шаг 3: Форматирование дерева в строку
    if format_name == 'stylish':
        result = format_stylish(diff_tree)
    # elif format_name == 'plain': # Задел на будущее
    #     result = format_plain(diff_tree)
    # elif format_name == 'json': # Задел на будущее
    #     result = format_json(diff_tree)
    else:
        raise ValueError(f"Unsupported format: {format_name}")

    return result
