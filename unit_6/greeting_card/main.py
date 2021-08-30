from file2 import *


def main():
    print("from file1:")
    GreetingCard().greeting_msg()
    print()
    print("from file2:")
    BirthdayCard().greeting_msg()


if __name__ == "__main__":
    main()
