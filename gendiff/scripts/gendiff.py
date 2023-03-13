#!usr/bin/env python3
import json


def sort_for_diff(items):
    """
    Sort an array of differences with signs - +
    in alphabet order. If keys are similar, the first
    one will be a pair with sign -
    :param items: list
    :return: None
    """
    for limit in range(len(items) - 1, 0, -1):
        for i in range(limit):
            char1 = items[i][0]
            key1 = items[i][2:].split(': ')[0]
            key2 = items[i + 1][2:].split(': ')[0]
            if key1 > key2:
                items[i], items[i + 1] = items[i + 1], items[i]
            if key1 == key2 and char1 == '+':
                items[i], items[i + 1] = items[i + 1], items[i]


def generate_diff(first_path, second_path):
    first_file = open(first_path)
    first_data = json.load(first_file)
    second_file = open(second_path)
    second_data = json.load(second_file)
    first_set = set(first_data.items())
    second_set = set(second_data.items())
    first_file.close()
    second_file.close()
    first_unique = first_set - second_set
    second_unique = second_set - first_set
    common_items = first_set & second_set
    result = []
    for key, val in first_unique:
        result.append(f'- {key}: {val}')
    for key, val in second_unique:
        result.append(f'+ {key}: {val}')
    for key, val in common_items:
        result.append(f'  {key}: {val}')
    sort_for_diff(result)
    return '{\n' + '\n'.join(result) + '\n}'


# Second variety of func
    # for key,val in first_data.items():
    #     val_in_2data = second_data.pop(key, None)
    #     first_data.pop(key)
    #     if val_in_2data:
    #         if val == val_in_2data:
    #             result.append(f'  {key}: {val}')
    #         if val != val_in_2data:
    #             result.append(f'- {key}: {val}')
    #             result.append(f'+ {key}: {val_in_2data}')
    #     else:
    #         result.append(f'- {key}: {val}')
    # return result

    # Third variety of func
    # first_data = []
    # second_data = []
    # first_file = json.load(open(first_path))
    # for key, val in zip(first_file.readline()):
    #     first_data.append((key, val))
    # first_file.close()
    # second_file = json.load(open(second_path))
    # for key, val in zip(second_file.readline()):
    #     second_data.append((key, val))
    # second_file.close()
    # result = []
    # while len(first_data) > 1 or len(second_data) > 1:
    #     match first_data:
    #         case True:
    #             '''
    #             If first_data isn't empty, func compare two keys and
    #             values and add them to result with relevant sign
    #             '''
    #             current_item = str(first_data.pop(0))
    #             second_item_key = current_item.split(': ')[0]
    #             items_index_in_2_data = second_data.index(current_item)
    #             if items_index_in_2_data != -1:
    #                 item_in_2_data = second_data.pop(items_index_in_2_data)
    #                 if current_item != item_in_2_data:
    #                     result.append(f'- {current_item}')
    #                     result.append(f'+ {item_in_2_data}')
    #                     continue
    #                 else:
    #                     result.append(f'  {current_item}')
    #             else:
    #                 result.append(f'- {current_item}')
