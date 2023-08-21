#!usr/bin/env python3
from gendiff.diff_tools import DiffObject


def format_stylish(obj, tabs=1):
    # Добавить сортировку obj по ключу
    if isinstance(obj, DiffObject):
        items = obj.get_diff_list()
        return "{\n" + '\n'.join([f'{tabs * "  "}{key}: {format_stylish(value, tabs + 2)}'
                                  for item in items for key, value in item.items()]) + '\n' + (tabs - 1) * "  " + "}"
    elif isinstance(obj, (list, tuple)):
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


# def generate_diff(first_path, second_path):
#     first_file_format = first_path.split('.')[-1]
#     second_file_format = second_path.split('.')[-1]
#     if first_file_format == 'json':
#         first_data = json.load(open(first_path))
#     else:
#         first_data = safe_load(open(first_path))
#     if second_file_format == 'json':
#         second_data = json.load((open(second_path)))
#     else:
#         second_data = safe_load(open(second_path))
#     diff = build_diff(first_data, second_data)
#     return diff


# print(format_stylish(generate_diff('tree_file2.json', 'tree_file1.json')))
