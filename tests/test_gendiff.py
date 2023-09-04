from gendiff import generate_diff
import os
import pytest


def get_fixture(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def get_expected_value(filename):
    with open(get_fixture(filename)) as f:
        return f.read()


first_json = 'tree_file1.json'
second_json = 'tree_file2.json'
first_yaml = 'tree_file1.yaml'
second_yml = 'tree_file2.yml'
correct_style = 'correct_stylish_diff.txt'
correct_plain = 'correct_plain_diff.txt'
correct_jsonify = 'correct_jsonify_diff.json'


@pytest.mark.parametrize('first_path,second_path,correct,output_format',
                         [(first_json, second_json, correct_plain, 'plain'),
                          (first_yaml, second_yml, correct_plain, 'plain'),
                          (first_json, second_yml, correct_jsonify, 'json'),
                          (first_yaml, second_json, correct_style, 'stylish')])
def test_generate_diff(first_path, second_path, correct, output_format):
    first_file = get_fixture(first_path)
    second_file = get_fixture(second_path)
    if output_format == 'stylish':
        expected = get_expected_value(correct).strip()
    else:
        expected = get_expected_value(correct)
    assert generate_diff(first_file, second_file, output_format) == expected
