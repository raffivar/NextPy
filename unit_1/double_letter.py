def double(char):
    return char + char


def double_letter(my_str):
    return ''.join(list(map(double, my_str)))


print(double_letter("python"))
print(double_letter("we are the champions!"))
