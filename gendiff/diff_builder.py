# hexlet_code/diff_builder.py

def build_diff_tree(data1, data2):
    """Строит дерево различий между двумя словарями (улучшенная структура)."""
    keys = sorted(list(data1.keys() | data2.keys()))
    diff_tree = []

    for key in keys:
        node = {'key': key}
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data1:
            node['type'] = 'added'
            node['value'] = value2  # Используем 'value' для нового значения
        elif key not in data2:
            node['type'] = 'removed'
            node['value'] = value1  # Используем 'value' для старого значения
        elif isinstance(value1, dict) and isinstance(value2, dict):
            node['type'] = 'nested'
            node['children'] = build_diff_tree(value1, value2)
        elif value1 == value2:
            node['type'] = 'unchanged'
            # ИСПРАВЛЕНО E501: Комментарий перенесен на строку выше
            # Используем 'value' для неизмененного значения
            node['value'] = value1
        else:
            node['type'] = 'changed'
            node['old_value'] = value1
            node['new_value'] = value2

        diff_tree.append(node)

    return diff_tree
