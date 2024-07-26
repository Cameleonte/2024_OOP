def solution():

    def integers():
        curr_num = 1
        while True:
            yield curr_num
            curr_num += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        res = []
        for num in range(0, n):
            res.append(next(seq))
        return res

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
