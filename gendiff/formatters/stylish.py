SYMBOL_STATUS = {'added': '+ ', 'removed': '- ', 'not changed': '  '}


def get_status_key(key, status):
    return f'{SYMBOL_STATUS[status]}{key}'


def build_stylish_tree(diff):
    sorted_diff = diff.sort()
    tree = {}
    for item in sorted_diff:
        for key, val in item.items():
            status = val[0]
            value = val[1]
            if isinstance(value, dict):
                value = add_identities_for_dict(value)
            if status == 'updated':
                if str(type(value)) == "<class 'diff_tools.DiffObject'>":
                    new_key = get_status_key(key, 'not changed')
                    tree[new_key] = build_stylish_tree(value)
                else:
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
        return "{\n" + '\n'.join([f'{tabs * "  "}{key}: {get_stylish_stdout(value, tabs + 2)}'
                                  for key, value in diff.items()]) + '\n' + (tabs - 1) * "  " + "}"
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
