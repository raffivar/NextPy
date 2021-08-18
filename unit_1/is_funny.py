def is_funny(string):
    return len(list(filter(lambda char: char not in 'ha', string))) == 0


print(is_funny("hahahahahaha"))
