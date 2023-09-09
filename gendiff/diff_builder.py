def get_node_type(first_val, second_val):
    if first_val == second_val:
        return 'not changed'
    elif isinstance(first_val, dict) and isinstance(second_val, dict):
        return 'nested'
    else:
        return 'updated'


def get_inner_diff(key, status, first_val, second_val):
    inner_diff = {}

    if status == 'nested':
        inner_diff[key] = (status, build_diff(first_val, second_val))
    if status == 'not changed' or status == 'added':
        inner_diff[key] = (status, second_val)
    if status == 'removed':
        inner_diff[key] = (status, first_val)
    if status == 'updated':
        inner_diff[key] = (status, (first_val, second_val))
    return inner_diff


def walk_keys(key_set, first_data, second_data, status=None):
    acc = []
    for key in key_set:
        first_val = first_data.get(key)
        second_val = second_data.get(key)
        changes_status = get_node_type(first_val, second_val) if not status\
            else status
        inner_diff = get_inner_diff(key, changes_status, first_val, second_val)
        acc.append(inner_diff)
    return acc


def sort_by_key(item):
    for key in item:
        return key


def build_diff(first_data, second_data):
    result = []
    first_set = set(first_data.keys())
    second_set = set(second_data.keys())
    common_keys = first_set & second_set
    removed_keys = first_set - second_set
    added_keys = second_set - first_set
    updated_items = walk_keys(common_keys, first_data, second_data)
    added_items = walk_keys(added_keys, first_data, second_data, 'added')
    removed_items = walk_keys(removed_keys, first_data, second_data, 'removed')
    result.extend(updated_items)
    result.extend(added_items)
    result.extend(removed_items)

    return list(sorted(result, key=sort_by_key))
