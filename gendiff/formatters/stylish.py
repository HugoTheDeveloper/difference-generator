SYMBOL_STATUS = {'added': '+ ', 'removed': '- ',
                 'not changed': '  ', 'nested': '  '}


def get_status_key(key, status):
    return f'{SYMBOL_STATUS[status]}{key}'


def build_stylish_tree(diff):
    tree = {}
    for item in diff:
        for key, val in item.items():
            status, value = val[0], val[1]
            if isinstance(value, dict):
                value = add_identities_for_dict(value)
            if status == 'nested':
                new_key = get_status_key(key, status)
                new_val = build_stylish_tree(value)
                tree[new_key] = new_val
            if status == 'updated':
                first_key = get_status_key(key, 'removed')
                second_key = get_status_key(key, 'added')
                first_val = value[0] # noqa never could be called as key for dict
                second_val = value[1] # noqa
                tree[first_key] = first_val
                tree[second_key] = second_val
            else:
                new_key = get_status_key(key, status)
                tree[new_key] = value
    return tree


def add_identities_for_dict(dic):
    updated_dic = {}
    for key, val in dic.items():
        if isinstance(val, dict):
            val = add_identities_for_dict(val)
        updated_dic[f'  {key}'] = val
    return updated_dic


def get_stylish_stdout(diff, tabs=1):
    if isinstance(diff, (list, tuple)):
        return "[" + ",".join([get_stylish_stdout(item) for item in diff]) + "]"
    elif isinstance(diff, dict):
        return "{\n" + '\n'.join([f'{tabs * "  "}{key}: '
                                  f'{get_stylish_stdout(value, tabs + 2)}'
                                  for key, value in diff.items()]) \
            + '\n' + (tabs - 1) * "  " + "}"
    elif isinstance(diff, str):
        return f'{diff}'
    elif isinstance(diff, bool):
        return str(diff).lower()
    elif diff is None:
        return "null"
    else:
        return str(diff)


def format_stylish(diff):
    stylish_tree = build_stylish_tree(diff)
    return get_stylish_stdout(stylish_tree)
