from gendiff import *
import os
import pytest


def get_fixture(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


@pytest.fixture(scope='module')
def first_json():
    return get_fixture('tree_file1.json')


@pytest.fixture(scope='module')
def second_json():
    return get_fixture('tree_file2.json')


@pytest.fixture(scope='module')
def first_yaml():
    return get_fixture('tree_file1.yaml')


@pytest.fixture(scope='module')
def second_yml():
    return get_fixture('tree_file2.yml')


@pytest.fixture(scope='module')
def correct_stylish_data():
    with open(get_fixture('correct_stylish_diff.txt'), 'r') as f:
        return f.read().strip()


@pytest.fixture(scope='module')
def correct_plain_data():
    with open(get_fixture('correct_plain_diff.txt')) as f:
        return f.read()


@pytest.fixture(scope='module')
def correct_jsonify_data():
    with open(get_fixture('correct_jsonify_diff.json')) as f:
        return f.read()


def test_generate_diff_plain(first_json, second_json, first_yaml, second_yml, correct_plain_data):
    expected = correct_plain_data
    assert generate_diff(first_json, second_json, 'plain') == expected
    assert generate_diff(first_yaml, second_yml, 'plain') == expected
    assert generate_diff(first_json, second_yml, 'plain') == expected


def test_generate_diff_jsonify(first_json, second_yml, correct_jsonify_data):
    expected = correct_jsonify_data
    assert generate_diff(first_json, second_yml, 'json') == expected


def test_generate_diff_stylish(first_json, second_yml, correct_stylish_data):
    expected = correct_stylish_data
    assert generate_diff(first_json, second_yml, 'stylish') == expected
