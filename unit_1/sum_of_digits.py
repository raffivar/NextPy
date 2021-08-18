from functools import reduce


def num_to_digits(num):
    return list(int(i) for i in str(num))


def add(num1, num2):
    return int(num1) + int(num2)


def sum_of_digits(num):
    return reduce(add, num_to_digits(num))


print(sum_of_digits(104))
