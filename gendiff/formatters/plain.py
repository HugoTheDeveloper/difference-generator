def prepare_value_to_json_style(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    else:
        return str(value)


def get_plain_stdout(key, val, cur_path):
    path = f'{cur_path}.{key}' if cur_path else key
    front_sample = f"Property '{path}' was"
    status = val[0]
    value = val[1]
    if status == 'updated':
        first_val = prepare_value_to_json_style(value[0])
        second_val = prepare_value_to_json_style(value[1])
        return f"{front_sample} updated: From {first_val} to {second_val}\n"
    if status == 'removed':
        return f'{front_sample} removed\n'
    if status == 'added':
        value = prepare_value_to_json_style(value)
        return f"{front_sample} added with value: {value}\n"


def skip_unchanged_keys(diff_item):
    for val in diff_item.values():
        status = val[0]
        if status == 'not changed':
            return False
        return True


def format_plain(diff, cur_path=''):
    result = ''
    sorted_diff = list(filter(skip_unchanged_keys, diff))
    for item in sorted_diff:
        for key, val in item.items():
            status = val[0]
            if status == 'nested':
                new_path = str(key) if not cur_path else f'{cur_path}.{key}'
                result += format_plain(val[1], new_path)
            else:
                result += get_plain_stdout(key, val, cur_path)
    if not cur_path:
        # Fork is aimed to remove last \n from result
        return result[:-1]
    return result
