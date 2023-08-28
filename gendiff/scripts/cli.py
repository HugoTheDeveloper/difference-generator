import argparse


def parse():
    comparator = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    comparator.add_argument('first_file')
    comparator.add_argument('second_file')
    comparator.add_argument('-f', '--format', help='set format of output',
                            default='stylish', )
    return comparator.parse_args()
