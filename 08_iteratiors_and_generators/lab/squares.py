# def squares(n):
#     new_list = []
#     for num in range(1, n + 1):
#         new_list.append(num * num)
#     return new_list

def squares(n):
    curr_num = 0
    while curr_num < n:
        curr_num += 1
        yield curr_num * curr_num


print(list(squares(5)))
