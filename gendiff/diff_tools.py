class DiffObject():
    def __init__(self):
        self.diff = []

    def get_diff_list(self):
        return self.diff

    def append(self, value):
        self.diff.append(value)

    def _sort(self):
        """
        sort diff object by key
        :return: list
        """
        result = list(sorted(self.get_diff_list(), key=lambda x: x.keys()))
        return result


