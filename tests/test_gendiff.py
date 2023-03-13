from gendiff.scripts.gendiff import *


correct_diff_between_first_and_second = '{\n- follow: false\n  host: hexlet.io\n' \
                                        '- proxy: 123.234.53.22\n- timeout: 50\n' \
                                        '+ timeout: 20\n+ verbose: true\n}'
file_path1 = 'tests/fixtures/file1.json'
file_path2 = 'tests/fixtures/file2.json'

# def test_gendiff():
#     assert generate_diff('tests.fixtures.file1.json', 'tests.fixtures.file2.json') == correct_diff_between_first_and_second


print(generate_diff(file_path1, file_path2))