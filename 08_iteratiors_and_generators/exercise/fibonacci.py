def fibonacci():
    num, next_num = 0, 1
    while True:
        yield num
        curr_num = num + next_num
        num, next_num = next_num, curr_num


generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
