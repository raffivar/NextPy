def combine_coins(coin, numbers):
    res_list = []
    for num in numbers:
        res_list.append(coin + str(num))
    return ', '.join(res_list)


def combine_coins2(coin, numbers):
    return ', '.join(coin + str(num) for num in numbers)


print(combine_coins2('$', range(5)))
