from gendiff.scripts.parser_json import *


def test_generate_diff_stylish():
    with open('fixtures/correct_diff_between_1and2.txt') as correct_diff_between_1and2:
        assert format_stylish(generate_diff(  # test json-json comparison
            'fixtures/tree_file1.json', 'fixtures/tree_file2.json')) == ''.join(correct_diff_between_1and2.readlines())
        assert format_stylish(generate_diff(  # test yaml-yaml comparison
            'fixtures/tree_file1.yaml', 'fixtures/tree_file2.yaml')) == ''.join(correct_diff_between_1and2.readlines())
    with open('fixtures/correct_diff_between_2and1.txt') as correct_diff_between_2and1:
        assert format_stylish(generate_diff(  # test json-yaml comparison
            'fixtures/tree_file2.json', 'fixtures/tree_file1.yaml')) == ''.join(correct_diff_between_2and1.readlines())


# test_generate_diff_stylish()

# with open('fixtures/correct_diff_between_1and2.txt') as correct_diff_between_1and2:
#     print(correct_diff_between_1and2.readlines())