# hexlet_code/formatters/plain.py

def format_plain_value(value):
    """Конвертирует значение в строку для plain формата."""
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()  # true / false
    # Числа и другие типы конвертируются в строку как есть
    return str(value)


def format_plain(diff_tree):
    """Форматирует дерево различий в стиль 'plain'."""

    def walk(nodes, path_prefix=''):
        """Рекурсивно обходит дерево и строит строки plain вывода."""
        lines = []
        sorted_nodes = sorted(nodes, key=lambda node: node['key'])

        for node in sorted_nodes:
            node_type = node['type']
            current_path = f"{path_prefix}{node['key']}"

            if node_type == 'nested':
                # ИСПРАВЛЕНО E501: Выносим new_prefix
                new_prefix = f"{current_path}."
                lines.extend(walk(node['children'], path_prefix=new_prefix))
            elif node_type == 'added':
                formatted_value = format_plain_value(node['value'])
                lines.append(
                    f"Property '{current_path}' was added with value: {formatted_value}" # noqa E501
                )
            elif node_type == 'removed':
                lines.append(f"Property '{current_path}' was removed")
            elif node_type == 'changed':
                formatted_old = format_plain_value(node['old_value'])
                formatted_new = format_plain_value(node['new_value'])
                lines.append(
                    f"Property '{current_path}' was updated. From {formatted_old} to {formatted_new}" # noqa E501
                )

        return lines

    plain_lines = walk(diff_tree)
    return "\n".join(plain_lines)
