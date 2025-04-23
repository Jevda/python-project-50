# hexlet_code/formatters/json.py
import json


def format_json(diff_tree):
    """Форматирует дерево различий в JSON строку."""
    # Используем стандартную библиотеку json для сериализации
    # indent=4 для красивого вывода (pretty-print)
    # ensure_ascii=False может понадобиться для не-ASCII символов,
    # но пока не нужно
    return json.dumps(diff_tree, indent=4)