def get_fibo():
    num1 = 0
    num2 = 1

    yield num1
    yield num2

    while True:
        total = num1 + num2
        num1 = num2
        num2 = total
        yield total


def main():
    fibo_gen = get_fibo()
    for i in range(0, 10):
        print(next(fibo_gen))


if __name__ == "__main__":
    main()
