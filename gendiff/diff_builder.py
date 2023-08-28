def compare_vals(first_val, second_val):
    status = None
    if first_val != 'Not in dic' and second_val != 'Not in dic':
        if first_val == second_val:
            status = 'not changed'
        else:
            if isinstance(first_val, dict) and isinstance(second_val, dict):
                status = 'nested'
            else:
                status = 'updated'

    if first_val == 'Not in dic':
        status = 'added'

    if second_val == 'Not in dic':
        status = 'removed'
    return status


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
        if (isinstance(first_val, dict) and not isinstance(second_val, dict)
                or not isinstance(first_val, dict) and isinstance(second_val, dict)): # noqa there is no possibility to make a line transition without linter's remarks
            inner_diff[key] = (status, (first_val, second_val))
        else:
            inner_diff[key] = (status, (first_val, second_val))
    return inner_diff


def build_diff(first_data, second_data):
    result = []
    all_keys = list(sorted(get_all_keys(first_data, second_data)))
    for key in all_keys:
        first_val = first_data.get(key, 'Not in dic')
        second_val = second_data.get(key, 'Not in dic')
        changes_status = compare_vals(first_val, second_val)
        inner_diff = get_inner_diff(key, changes_status, first_val, second_val)
        result.append(inner_diff)
    return result
