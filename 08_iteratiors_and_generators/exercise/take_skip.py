class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.curr_num = 0
        self.curr_step = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        while self.curr_num < self.count:
            self.curr_step += self.step
            self.curr_num += 1
            return self.curr_step
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
