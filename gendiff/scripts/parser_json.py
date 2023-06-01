#!usr/bin/env python3
import json
from yaml import safe_load
from gendiff.engine import build_diff_dic


def format_stylish(obj, tabs=1):
    if isinstance(obj, (list, tuple)):
        return "[" + ",".join([format_stylish(item) for item in obj]) + "]"
    elif isinstance(obj, dict):
        return "{\n" + '\n'.join([f'{tabs * "  "}{key}: {format_stylish(value, tabs + 2)}'
                                  for key, value in obj.items()]) + '\n' + (tabs - 1) * "  " + "}"
    elif isinstance(obj, str):
        return f'{obj}'
    elif isinstance(obj, bool):
        return str(obj).lower()
    elif obj is None:
        return "null"
    else:
        return str(obj)


def generate_diff(first_path, second_path):
    first_file_format = first_path.split('.')[-1]
    second_file_format = second_path.split('.')[-1]
    if first_file_format == 'json':
        first_data = json.load(open(first_path))
    else:
        first_data = safe_load(open(first_path))
    if second_file_format == 'json':
        second_data = json.load((open(second_path)))
    else:
        second_data = safe_load(open(second_path))
    diff = build_diff_dic(first_data, second_data)
    return diff


# print(format_stylish(generate_diff('tree_file2.json', 'tree_file1.json')))
