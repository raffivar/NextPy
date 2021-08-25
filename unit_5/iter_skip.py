def main():
    numbers = iter(list(range(1, 101)))
    for i in numbers:
        try:
            next(numbers)
            next(numbers)
            print(i)
        except StopIteration:
            break


if __name__ == "__main__":
    main()
