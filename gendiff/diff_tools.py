def sort_by_key(item):
    for key in item:
        return key


class DiffObject:
    def __init__(self):
        self.diff = []

    def get_diff_list(self):
        return self.diff

    def append(self, value):
        self.diff.append(value)

    def sort(self):
        result = list(sorted(self.get_diff_list(), key=sort_by_key))
        return result
