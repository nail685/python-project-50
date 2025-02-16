from gendiff.build_diff import build_diff
from gendiff.formatters.__init__ import select_formatter
from gendiff.parser import parser


def generate_diff(path_file1, path_file2, format_name='stylish'):
    file1 = parser(path_file1)
    file2 = parser(path_file2)
    diff = build_diff(file1, file2)
    select_formatters = select_formatter(diff, format_name)
    return select_formatters
