from functools import reduce

with open("names.txt", "r") as file:
    print(max(file.read().split(), key=lambda name: len(name)))

with open("names.txt", "r") as file:
    print(reduce(lambda cur_len, next_str: cur_len + len(next_str), file.read().split(), 0))

with open("names.txt", "r") as file:
    names = file.read().split()
    min_length = len(min(names, key=lambda name: len(name)))
    print(' '.join(list(filter(lambda name: len(name) == min_length, names))))

with open("names.txt", "r") as file:
    print(' '.join(list(map(lambda name: str(len(name)), file.read().split()))))

with open("names.txt", "r") as file:
    print(' '.join(list(filter(lambda name: len(name) == 4, file.read().split()))))
