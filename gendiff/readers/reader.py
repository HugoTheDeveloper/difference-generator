import json
from yaml import safe_load
import os

FORMATTER = {'.json': json.loads, '.yaml': safe_load, '.yml': safe_load}


def get_file_and_extension(path):
    path = os.path.join(path)
    _, extension = os.path.splitext(path)
    if not FORMATTER.get(extension):
        raise ValueError("This file extension is not supported."
                         " Only 'json', 'yaml' and 'yml' files.")
    data = open(path).read()
    return data, extension


def parse_file(data, extension):
    parsed_data = FORMATTER[extension](data)
    return parsed_data


def read_data(path):
    file, extension = get_file_and_extension(path)
    data = parse_file(file, extension)
    return data
