class dictionary_iter:

    def __init__(self, my_dictionary: dict):
        self.my_dict_tuple = tuple(my_dictionary.items())
        self.curr_idx = - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_idx += 1
        while self.curr_idx < len(self.my_dict_tuple):
            return self.my_dict_tuple[self.curr_idx]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
