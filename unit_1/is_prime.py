def is_prime(number):
    return len(list(filter(lambda x: number % x == 0, range(2, number // 2 + 1)))) == 0


print(is_prime(4))
print(is_prime(42))
print(is_prime(43))
