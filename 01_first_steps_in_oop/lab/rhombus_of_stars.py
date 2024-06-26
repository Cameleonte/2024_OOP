rows = int(input())


def creating_upper_part():
    for row in range(1, rows + 1):
        print(' ' * (rows - row) + '* ' * row)


creating_upper_part()


def creating_bottom_part():
    for row in range(rows - 1, 0, - 1):
        print(' ' * (rows  - row) + '* ' * row)


creating_bottom_part()
