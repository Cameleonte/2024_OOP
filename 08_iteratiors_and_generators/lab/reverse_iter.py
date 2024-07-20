class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.current_num = len(self.iterable)
        self.end_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_num -= 1
        if self.current_num >= self.end_idx:
            return self.iterable[self.current_num]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
