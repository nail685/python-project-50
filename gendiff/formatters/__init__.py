from gendiff.formatters.json import json_formatter
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def select_formatter(diff, format_name):
    match format_name:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return json_formatter(diff)
        case _:
            return stylish(diff)
