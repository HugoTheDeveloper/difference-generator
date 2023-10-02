from gendiff import generate_diff
import os
import pytest


def get_fixture(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def get_expected_value(filename):
    with open(get_fixture(filename)) as f:
        return f.read()


@pytest.mark.parametrize('first_path,second_path,correct,output_format',
                         [('tree_file1.json', 'tree_file2.json', 'correct_plain_diff.txt', 'plain'),
                          ('tree_file1.yaml', 'tree_file2.yml', 'correct_plain_diff.txt', 'plain'),
                          ('tree_file1.json', 'tree_file2.yml', 'correct_jsonify_diff.json', 'json'),
                          ('tree_file1.yaml', 'tree_file2.json', 'correct_stylish_diff.txt', 'stylish')])
def test_generate_diff(first_path, second_path, correct, output_format):
    first_file = get_fixture(first_path)
    second_file = get_fixture(second_path)
    expected = get_expected_value(correct).strip()
    assert generate_diff(first_file, second_file, output_format) == expected
