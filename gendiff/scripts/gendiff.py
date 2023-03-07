import argparse


def parse():
    comparator = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    comparator.add_argument('first_file')
    comparator.add_argument('second_file')
    return comparator.parse_args()


if __name__ == '__main__':
    parse()