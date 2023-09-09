SYMBOL_STATUS = {'added': '+ ', 'removed': '- ',
                 'not changed': '  ', 'nested': '  '}


def get_status_key(key, status):
    return f'{SYMBOL_STATUS[status]}{key}'


def build_stylish_tree(diff, depth=1):
    tree = {}
    for item in diff:
        for key, val in item.items():
            status, value = val[0], val[1]
            if status == 'nested':
                new_key = get_status_key(key, status)
                new_val = build_stylish_tree(value, depth + 1)
                tree[new_key] = new_val
                continue
            if status == 'updated':
                first_key = get_status_key(key, 'removed')
                second_key = get_status_key(key, 'added')
                first_val = to_str(value[0], depth)
                second_val = to_str(value[1], depth)
                tree[first_key] = first_val
                tree[second_key] = second_val
            if status == 'removed' or status == 'added' or\
                    status == 'not changed':
                new_key = get_status_key(key, status)
                tree[new_key] = to_str(value, depth)
    return tree


def to_str(value, depth=0):
    if isinstance(value, dict):
        prepared_dict = add_identities(value)
        tab = depth * 2 + 1
        return get_stylish_output(prepared_dict, tab)
    elif isinstance(value, (list, tuple)):
        return f"[{','.join(value)}]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)


def add_identities(dic):
    updated_dic = {}
    for key, val in dic.items():
        if isinstance(val, dict):
            val = add_identities(val)
        updated_dic[f'  {key}'] = val
    return updated_dic


def get_stylish_output(diff, tabs_count=1):
    tab = '  '
    raw_content = [f'{tabs_count * tab}{key}: '
                    f'{get_stylish_output(value, tabs_count + 2) if isinstance(value, dict) else value}'  # noqa
                    for key, value in diff.items()]
    content = '\n'.join(raw_content)
    return f"{{\n{content}\n{(tabs_count - 1) * tab}}}"


def format_stylish(diff):
    stylish_tree = build_stylish_tree(diff)
    return get_stylish_output(stylish_tree)
