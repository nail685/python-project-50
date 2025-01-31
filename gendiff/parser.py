from json import load
from yaml import safe_load


def parser(file):
    if file.endswith('.json'):
        with open(file) as new_file:
            return load(new_file)
    elif file.endswith('.yaml') or file.endswith('.yml'):
        with open(file) as new_file:
            return safe_load(new_file)
