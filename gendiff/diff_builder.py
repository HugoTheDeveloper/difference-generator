# import json
# from gendiff.formatters.stylish import format_stylish, build_stylish_tree
# from gendiff.formatters.plain import format_plain


def compare_vals(first_dic, second_dic, key):
    first_val = first_dic.get(key, 'Not in dic')
    second_val = second_dic.get(key, 'Not in dic')
    if first_val != 'Not in dic' and second_val != 'Not in dic':
        if first_val == second_val:
            return 'not changed'
        else:
            if isinstance(first_val, dict) and isinstance(second_val, dict):
                return 'nested'
            return 'updated'

    if first_val == 'Not in dic':
        return 'added'

    if second_val == 'Not in dic':
        return 'removed'


def get_all_keys(first_dic, second_dic):
    united_dic = first_dic.copy()
    united_dic.update(second_dic)
    return [key for key in united_dic.keys()]


def get_inner_diff(key, status, first_val, second_val):
    inner_diff = {}

    if status == 'nested':
        inner_diff[key] = (status, build_diff(first_val, second_val))
    if status == 'not changed' or status == 'added':
        inner_diff[key] = (status, second_val)
    if status == 'removed':
        inner_diff[key] = (status, first_val)
    if status == 'updated':
        # Fork for case, when dict value was updated to non-dict value
        if ((isinstance(first_val, dict) and not isinstance(second_val, dict)) or
                not isinstance(first_val, dict) and isinstance(second_val, dict)):
            inner_diff[key] = (status, (first_val, second_val))
        else:
            inner_diff[key] = (status, (first_val, second_val))
    return inner_diff


def build_diff(first_data, second_data):
    result = []
    all_keys = list(sorted(get_all_keys(first_data, second_data)))
    for key in all_keys:
        changes_status = compare_vals(first_data, second_data, key)
        first_val = first_data.get(key, 'Not in dic')
        second_val = second_data.get(key, 'Not in dic')
        inner_diff = get_inner_diff(key, changes_status, first_val, second_val)
        result.append(inner_diff)
    return result

# def get_file(path):
#     with open(path) as f:
#         return json.loads(f.read())

# data1= get_file('../tests/fixtures/tree_file1.json')
# data2 = get_file('../tests/fixtures/tree_file2.json')
# print(format_stylish(build_diff(data1, data2)))
