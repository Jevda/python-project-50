# hexlet_code/diff_builder.py

def build_diff_tree(data1, data2):
    """Строит дерево различий между двумя словарями."""
    # Объединяем и сортируем ключи
    keys = sorted(list(data1.keys() | data2.keys()))
    diff_tree = []

    for key in keys:
        node = {'key': key}

        if key not in data1:
            node['type'] = 'added'
            node['value'] = data2[key]
        elif key not in data2:
            node['type'] = 'removed'
            node['value'] = data1[key]
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            node['type'] = 'nested'
            node['children'] = build_diff_tree(data1[key], data2[key])
        elif data1[key] == data2[key]:
            node['type'] = 'unchanged'
            node['value'] = data1[key]
        else:
            node['type'] = 'changed'
            node['old_value'] = data1[key]
            node['new_value'] = data2[key]

        diff_tree.append(node)

    return diff_tree
