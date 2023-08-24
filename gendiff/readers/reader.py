import json
from yaml import safe_load
import os


FORMATTER = {'.json': json.loads, '.yaml': safe_load, '.yml': safe_load}


def read_file_(path):
    path = os.path.join(path)
    if not os.path.exists(path):
        raise FileExistsError("This file doesn't exist or path is wrong")
    _, extension = os.path.splitext(path)
    if not FORMATTER.get(extension):
        raise Exception("This file extension is not supported."
                        " Only 'json', 'yaml' and 'yml' files.")
    with open(path) as f:
        data = FORMATTER[extension](f.read())
    return data
