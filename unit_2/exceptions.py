def stop_iteration_error():
    def simple_generator():
        yield "foo"
        yield "bar"

    g = simple_generator()
    next(g)
    next(g)
    next(g)


def zero_division_error():
    val = 5 / 0


def assertion_error():
    x = 1
    y = 0
    assert y != 0, "Invalid Operation"  # denominator can't be 0
    print(x / y)


def import_error():
    print("Program to demonstrate to handle ImportError:")
    print("\n")
    from crypt import mksalt


def key_error():
    dictionary = {'key1': 'value1', 'key2': 'value2'}
    print(dictionary["key3"])


def syntax_error():  # modify to "iff" to get error
    x = 10
    if x % 2 == 0:
        print('X is even')
    else:
        print('X is odd')


def indentation_error():  # indent one of the lines to get error
    x = 5
    x += 1


def type_error():
    my_set = {'value1', 'value2'}
    print(my_set["fake_key"])


def main():
    pass


if __name__ == "__main__":
    main()
