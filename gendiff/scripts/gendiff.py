import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files '
                                             'and shows a difference.')
parser.add_argument('integers', metavar='first_file',
                    help='First file for diff')
parser.add_argument('integers', metavar='second_file', type=str,
                    help='Second file for diff')
parser.add_argument('-f FORMAT', metavar='--format FORMAT',
                    help='set format of output')

args = parser.parse_args()
