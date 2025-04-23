# hexlet_code/formatters/stylish.py
import itertools

# Константы для отступов и префиксов
INDENT_SIZE = 4
PREFIX_OFFSET = 2
PREFIXES = {'added': '+ ', 'removed': '- ', 'unchanged': '  '}


def get_indent(depth):
    """Возвращает строку отступа для заданной глубины."""
    return ' ' * (depth * INDENT_SIZE - PREFIX_OFFSET)


def format_value(value, depth):
    """Форматирует значение для вывода (с рекурсией для словарей)."""
    if isinstance(value, dict):
        # Если значение - словарь, форматируем его рекурсивно
        indent = get_indent(depth + 1)
        end_indent = ' ' * (depth * INDENT_SIZE)
        lines = ["{"]
        for key, val in value.items():
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{indent}  {key}: {formatted_val}")
        lines.append(end_indent + "}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        # Для остальных типов просто возвращаем строковое представление
        return str(value)


def format_stylish(diff_tree):
    """Форматирует дерево различий в стиль 'stylish'."""

    def walk(nodes, depth):
        """Рекурсивно обходит дерево и строит строки вывода."""
        lines = []
        indent = get_indent(depth)
        end_indent = ' ' * ((depth - 1) * INDENT_SIZE)  # Отступ для '}'

        for node in nodes:
            node_type = node['type']
            key = node['key']

            if node_type == 'nested':
                # Рекурсивный вызов для вложенных узлов
                children_lines = walk(node['children'], depth + 1)
                lines.append(f"{indent}  {key}: {children_lines}")
            elif node_type == 'changed':
                # Выводим две строки для измененного значения
                old_val_str = format_value(node['old_value'], depth)
                new_val_str = format_value(node['new_value'], depth)
                lines.append(f"{indent}- {key}: {old_val_str}")
                lines.append(f"{indent}+ {key}: {new_val_str}")
            else:
                # Для added, removed, unchanged - одна строка
                prefix = PREFIXES[node_type]
                value_str = format_value(node['value'], depth)
                lines.append(f"{indent}{prefix}{key}: {value_str}")

        # Собираем строки с правильными отступами и скобками
        result = itertools.chain("{", lines, [end_indent + "}"])
        return "\n".join(result)

    # Начинаем обход с глубины 1
    return walk(diff_tree, 1)
