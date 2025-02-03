from gendiff.parser import parser
from gendiff.build_diff import build_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_formatter


def generate_diff(path_file1, path_file2, format_name='stylish'):
    file1 = parser(path_file1)
    file2 = parser(path_file2)
    diff = build_diff(file1, file2)
    match format_name:
        case 'stylish':
            return stylish(diff)
        case 'plan':
            return plain(diff)
        case 'json':
            return json_formatter(diff)
        case _:
            return "Wrong format"


generate_diff('tests\fixtures\file1.json', 'tests\fixtures\file1.json', 'json')