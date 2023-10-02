def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)


def get_plain_output(key, val, cur_path, acc):
    path = f'{cur_path}.{key}' if cur_path else key
    front_sample = f"Property '{path}' was"
    status = val[0]
    value = val[1]
    if status == 'updated':
        first_val = to_str(value[0])
        second_val = to_str(value[1])
        acc.append(f"{front_sample} updated. From {first_val} to {second_val}")
    elif status == 'removed':
        acc.append(f'{front_sample} removed')
    elif status == 'added':
        value = to_str(value)
        acc.append(f"{front_sample} added with value: {value}")
    elif status == 'not changed':
        pass
    elif status == 'nested':
        new_path = str(key) if not cur_path else f'{cur_path}.{key}'
        acc.append(format_plain(val[1], new_path))
    else:
        raise ValueError('Incorrect status!')


def format_plain(diff, cur_path=''):
    result = []
    for item in diff:
        for key, val in item.items():
            get_plain_output(key, val, cur_path, result)
    return '\n'.join(result)
