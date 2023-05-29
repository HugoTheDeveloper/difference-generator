from gendiff.scripts.parser_json import *


correct_diff_between_first_and_second = '{\n- follow: False\n  host: hexlet.io\n' \
                                        '- proxy: 123.234.53.22\n- timeout: 50\n' \
                                        '+ timeout: 20\n+ verbose: True\n}'
correct_diff_between_second_and_first = '{\n+ follow: False\n  host: hexlet.io\n' \
                                        '+ proxy: 123.234.53.22\n- timeout: 20\n' \
                                        '+ timeout: 50\n- verbose: True\n}'
json_filepath1 = 'tests/fixtures/file1.json'
json_filepath2 = 'tests/fixtures/file2.json'

def test_gendiff():
    assert generate_diff(json_filepath1, json_filepath2) == \
           correct_diff_between_first_and_second
    assert generate_diff(json_filepath2, json_filepath1) == \
            correct_diff_between_second_and_first


