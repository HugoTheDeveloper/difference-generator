#!usr/bin/env python3
from yaml import safe_load
from parser_json import sort_for_diff


filepath1 = 'file1.yaml'
filepath2 = 'file2.yaml'


def generate_diff_yaml(first_path, second_path):
    first_file = safe_load(open(first_path))
    second_file = safe_load(open(second_path))
    first_set = set(first_file.items())
    second_set = set(second_file.items())
    first_unique = first_set - second_set
    second_unique = second_set - first_set
    common_items = first_set & second_set
    result = []
    for key, val in first_unique:
        result.append(f'- {key}: {val}')
    for key, val in second_unique:
        result.append(f'+ {key}: {val}')
    for key, val in common_items:
        result.append(f'  {key}: {val}')
    sort_for_diff(result)
    return '{\n' + '\n'.join(result) + '\n}'

print(generate_diff_yaml(filepath1, filepath2))
