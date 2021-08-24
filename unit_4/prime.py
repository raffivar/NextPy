def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    translate_gen = (num for num in range(n + 1, 2 ** 32) if is_prime(num))
    return next(translate_gen)


def main():
    print(first_prime_over(1000000))


if __name__ == "__main__":
    main()
