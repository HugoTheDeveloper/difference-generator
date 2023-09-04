def compare_vals(first_val, second_val):
    if first_val == second_val:
        return 'not changed'
    elif isinstance(first_val, dict) and isinstance(second_val, dict):
        return 'nested'
    else:
        return 'updated'


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
    first_set = set(first_data.keys())
    second_set = set(second_data.keys())
    all_keys = sorted(list(first_set | second_set))
    common_keys = first_set & second_set
    first_exclusive_keys = first_set - second_set
    second_exclusive_keys = second_set - first_set
    for key in all_keys:
        first_val = first_data.get(key)
        second_val = second_data.get(key)
        changes_status = None
        if key in common_keys:
            changes_status = compare_vals(first_val, second_val)
        if key in first_exclusive_keys:
            changes_status = 'removed'
        if key in second_exclusive_keys:
            changes_status = 'added'
        inner_diff = get_inner_diff(key, changes_status, first_val, second_val)
        result.append(inner_diff)

    return result
