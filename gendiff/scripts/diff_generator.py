#!usr/bin/env python3
from gendiff.diff_builder import build_diff
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.jsonify import format_json
from gendiff.readers.reader import read_file_


OUTPUT_FORMATTER = {'json': format_json,
                    'stylish': format_stylish, 'plain': format_plain}


def generate_diff(first_path, second_path, output_format):
    first_data = read_file_(first_path)
    second_data = read_file_(second_path)
    diff = build_diff(first_data, second_data)
    formatted_diff = OUTPUT_FORMATTER[output_format](diff)
    return formatted_diff
