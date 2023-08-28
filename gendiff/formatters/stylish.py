SYMBOL_STATUS = {'added': '+ ', 'removed': '- ',
                 'not changed': '  ', 'nested': '  '}


def get_status_key(key, status):
    return f'{SYMBOL_STATUS[status]}{key}'


def build_stylish_tree(diff):
    tree = {}
    for item in diff:
        for key, val in item.items():
            status, value = val[0], val[1]
            if status == 'nested':
                new_key = get_status_key(key, status)
                new_val = build_stylish_tree(value)
                tree[new_key] = new_val
                continue
            if status == 'updated':
                first_key = get_status_key(key, 'removed')
                second_key = get_status_key(key, 'added')
                first_val = validate_val(value[0])  # noqa never could be called as key for dict
                second_val = validate_val(value[1])  # noqa
                tree[first_key] = first_val
                tree[second_key] = second_val
            if status == 'removed' or status == 'added' or status == 'not changed':
                new_key = get_status_key(key, status)
                tree[new_key] = validate_val(value)
    return tree


def validate_val(value):
    if isinstance(value, dict):
        return add_identities_for_dict(value)
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(value) + "]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    else:
        return str(value)


def add_identities_for_dict(dic):
    updated_dic = {}
    for key, val in dic.items():
        if isinstance(val, dict):
            val = add_identities_for_dict(val)
        updated_dic[f'  {key}'] = val
    return updated_dic


def get_stylish_stdout(diff, tabs_count=1):
    tab = '  '
    content = [f'{tabs_count * tab}{key}: '
               f'{get_stylish_stdout(value, tabs_count + 2) if isinstance(value, dict) else value}'
               for key, value in diff.items()]
    return "{\n" + '\n'.join(content) + '\n' + (tabs_count - 1) * tab + "}"


def format_stylish(diff):
    stylish_tree = build_stylish_tree(diff)
    return get_stylish_stdout(stylish_tree)
