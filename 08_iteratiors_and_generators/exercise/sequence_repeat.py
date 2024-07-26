class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.curr_num = - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.number > 0:
            self.number -= 1
            self.curr_num += 1
            if self.curr_num == len(self.sequence):
                self.curr_num = 0
            return self.sequence[self.curr_num]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
