def reverse_text(some_string: str):
    curr_ch = len(some_string) - 1
    while curr_ch >= 0:
        yield some_string[curr_ch]
        curr_ch -= 1


for char in reverse_text("step"):
    print(char, end='')
