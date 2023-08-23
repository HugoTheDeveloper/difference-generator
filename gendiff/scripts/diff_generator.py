#!usr/bin/env python3
import json
from yaml import safe_load
import os
from gendiff.diff_builder import build_diff
from gendiff.formatters.plain import format_plain

FORMATTER = {'.json': json.loads, '.yaml': safe_load, '.yml': safe_load}


def generate_diff(first_path, second_path):
    first_path = os.path.join(first_path)
    second_path = os.path.join(second_path)
    _, first_file_extension = os.path.splitext(first_path)
    _, second_file_extension = os.path.splitext(second_path)
    with open(first_path) as f:
        first_data = FORMATTER[first_file_extension](f.read())
        with open(second_path) as fi:
            second_data = FORMATTER[second_file_extension](fi.read())
            diff = build_diff(first_data, second_data)
    return diff


print(format_plain(generate_diff('tree_file2.json', 'tree_file1.json')))
