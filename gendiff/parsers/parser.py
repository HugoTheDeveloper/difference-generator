import json
from yaml import safe_load

FORMATTER = {'.json': json.loads, '.yaml': safe_load, '.yml': safe_load}


def parse_data(data, extension):
    parsed_data = FORMATTER[extension](data)
    return parsed_data
