# hexlet_code/differ.py
from .diff_builder import build_diff_tree

# Импортируем функцию выбора форматера
from .formatters import get_formatter
from .parsers import parse_data


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Сравнивает два файла и возвращает строку с различиями
    в заданном формате.
    """
    # Шаг 1: Парсинг файлов
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)

    # Шаг 2: Построение внутреннего дерева различий
    diff_tree = build_diff_tree(data1, data2)

    # Шаг 3: Получение и вызов нужного форматера
    formatter = get_formatter(format_name)
    result = formatter(diff_tree)

    return result
