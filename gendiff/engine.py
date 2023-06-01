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


def build_diff_dic(first_data, second_data):
    diff = {}
    all_keys = first_data.copy()
    all_keys.update(second_data)
    for key in all_keys.keys():
        first_val = first_data.get(key, 'Not in dic')
        second_val = second_data.get(key, 'Not in dic')
        if isinstance(first_val, dict):
            if isinstance(second_val, dict):
                new_key = '  ' + key
                diff[new_key] = build_diff_dic(first_val, second_val)
                continue
            elif second_val == 'Not in dic':
                new_key = "- " + key
                diff[new_key] = build_diff_dic(first_val, first_val)
                continue
            else:
                diff['- ' + key] = first_val
                diff['+ ' + key] = second_val
                continue

        if isinstance(second_val, dict):
            if first_val == 'Not in dic':
                new_key = "+ " + key
                diff[new_key] = build_diff_dic(second_val, second_val)
                continue
            else:
                diff['- ' + key] = first_val
                diff['+ ' + key] = second_val
                continue

        changes_status = compare_vals(first_data, second_data, key)

        if changes_status == 'not changed':
            diff['  ' + key] = first_val
        if changes_status == 'updated':
            diff['- ' + key] = first_val
            diff['+ ' + key] = second_val
        if changes_status == 'removed':
            diff['- ' + key] = first_val
        if changes_status == 'added':
            diff['+ ' + key] = second_val
    diff = dict(sorted(diff.items(), key=lambda x: x[0][2:]))
    return diff
