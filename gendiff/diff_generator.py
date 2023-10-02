from gendiff.diff_builder import build_diff
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.jsonify import format_json
from gendiff.parsers.parser import parse_data, FORMATTER
import os


OUTPUT_FORMATTER = {'json': format_json,
                    'stylish': format_stylish, 'plain': format_plain}


def get_file_and_extension(path):
    path = os.path.join(path)
    _, extension = os.path.splitext(path)
    if not FORMATTER.get(extension):
        raise ValueError("This file extension is not supported."
                         " Only 'json', 'yaml' and 'yml' files.")
    data = open(path).read()
    return data, extension


def read_data(path):
    file, extension = get_file_and_extension(path)
    data = parse_data(file, extension)
    return data


def generate_diff(first_path, second_path, output_format='stylish'):
    if output_format not in OUTPUT_FORMATTER:
        raise ValueError('Incorrect output format - only stylish, json, plain.')
    first_data = read_data(first_path)
    second_data = read_data(second_path)
    diff = build_diff(first_data, second_data)
    formatted_diff = OUTPUT_FORMATTER[output_format](diff)
    return formatted_diff
