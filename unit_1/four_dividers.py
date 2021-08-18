def is_four_divider(num):
    return num % 4 == 0


def four_dividers(num):
    return list(filter(is_four_divider, range(1, num + 1)))


print(four_dividers(9))
print(four_dividers(3))
