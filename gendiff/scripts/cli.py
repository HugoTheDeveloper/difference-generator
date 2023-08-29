import argparse
from gendiff.diff_generator import *


def parse():
    comparator = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    comparator.add_argument('first_file')
    comparator.add_argument('second_file')
    comparator.add_argument('-f', '--format', help='set format of output',
                            default='stylish',
                            choices=['stylish', 'plain', 'json'])
    arguments = comparator.parse_args()
    style = arguments.format
    first_path = arguments.first_file
    second_path = arguments.second_file
    print(generate_diff(first_path, second_path, style))
