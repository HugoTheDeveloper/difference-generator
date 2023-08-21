import json
from diff_tools import DiffObject
from scripts.parser_json import format_stylish


def compare_vals(first_dic, second_dic, key):
    first_val = first_dic.get(key, 'Not in dic')
    second_val = second_dic.get(key, 'Not in dic')
    if first_val != 'Not in dic' and second_val != 'Not in dic':
        if first_val == second_val:
            return 'not changed'
        else:
            return 'updated'

    if first_val == 'Not in dic':
        return 'added'

    if second_val == 'Not in dic':
        return 'removed'


def get_all_keys(first_dic, second_dic):
    united_dic = first_dic.copy()
    united_dic.update(second_dic)
    return [key for key in united_dic.keys()]


def build_inner_diff(key, status, first_val, second_val):
    inner_diff = {}

    if status == 'not changed' or status == 'added':
        inner_diff[key] = (status, second_val)
    if status == 'removed':
        inner_diff[key] = (status, first_val)
    if status == 'updated':
        if isinstance(first_val, dict) or isinstance(second_val, dict):
            first_data = first_val if isinstance(first_val, dict) else {}
            second_data = second_val if isinstance(second_val, dict) else {}
            inner_diff[key] = (status, build_diff(first_data, second_data))
        else:
            inner_diff[key] = (status, (first_val, second_val))
    return inner_diff



def build_diff(first_data, second_data):
    result = DiffObject()
    all_keys = get_all_keys(first_data, second_data)
    for key in all_keys:
        changes_status = compare_vals(first_data, second_data, key)
        first_val = first_data.get(key, 'Not in dic')
        second_val = second_data.get(key, 'Not in dic')
        inner_diff = build_inner_diff(key, changes_status, first_val, second_val)
        result.append(inner_diff)
        # if isinstance(first_val, dict):
        #     if isinstance(second_val, dict):
        #         new_key = '  ' + key
        #         diff[new_key] = build_diff(first_val, second_val)
        #         continue
        #     elif second_val == 'Not in dic':
        #         new_key = "- " + key
        #         diff[new_key] = build_diff(first_val, first_val)
        #         continue
        #     else:
        #         diff['- ' + key] = first_val
        #         diff['+ ' + key] = second_val
        #         continue
        #
        # if isinstance(second_val, dict):
        #     if first_val == 'Not in dic':
        #         new_key = "+ " + key
        #         diff[new_key] = build_diff(second_val, second_val)
        #         continue
        #     else:
        #         diff['- ' + key] = first_val
        #         diff['+ ' + key] = second_val
        #         continue


    #     if changes_status == 'not changed':
    #         diff['  ' + key] = first_val
    #     if changes_status == 'updated':
    #         diff['- ' + key] = first_val
    #         diff['+ ' + key] = second_val
    #     if changes_status == 'removed':
    #         diff['- ' + key] = first_val
    #     if changes_status == 'added':
    #         diff['+ ' + key] = second_val
    # diff = dict(sorted(diff.items(), key=lambda x: x[0][2:]))
    return result


def get_file(path):
    with open(path) as f:
        return json.loads(f.read())


data1 = get_file('scripts/plain_file.json')
data2 = get_file('scripts/plain_file2.json')

diff= build_diff(data1, data2)
print(isinstance(format_stylish(diff), str))