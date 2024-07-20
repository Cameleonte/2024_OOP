class vowels:

    def __init__(self, some_string: str) -> None:
        self.some_string = some_string
        self.current_idx: int = - 1
        self.lst_vowels = ['a', 'o', 'u', 'e', 'i', 'y']
        self.string_vowels = [v for v in self.some_string if v.lower() in self.lst_vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx += 1
        if self.current_idx < len(self.string_vowels):
            return self.string_vowels[self.current_idx]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
