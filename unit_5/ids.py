import types


def check_id_valid(id_number):
    """Checks if an ID number is valid
    :param id_number: represents an ID number
    :type id_number: int
    :return: True if the id_number is valid, false otherwise_
    :rtype: bool"""
    id_list = list(map(int, (str(id_number))))
    # t = item (tuple) in enumerator, consisted of: (index, digit)
    # multiplying each digit with 2 powered by index % 2 (2^0 == 1, 2^1 == 2)
    id_mult = list(map(lambda t: t[1] * (2 ** (t[0] % 2)), enumerate(id_list)))
    # summing digits will work for all nums (even if n < 10)
    # safe to assume n is 2 digits max (max value is 18)
    id_united = list(map(lambda n: (n // 10 + n % 10), list(id_mult)))
    return sum(id_united) % 10 == 0


def get_next_id(curr_id=100000000 - 1):
    """Generator method that yields the next valid ID
    :param curr_id: the start ID - is incremented within the method
    :type curr_id: int"""
    end = 999999999
    while curr_id <= end:
        curr_id += 1
        if check_id_valid(curr_id):
            yield curr_id


class IDIterator:
    def __init__(self, start=100000000 - 1):
        """Inits the class with a default start ID
        :param start: the start ID
        :type start: int"""
        self._start = start
        self._end = 999999999
        self._id = self._start

    def __iter__(self):
        """Returns instance of self"""
        return self

    def __next__(self):
        """Gets next valid ID
        raise: StopIteration: raises an Exception"""
        while self._id <= self._end:
            self._id += 1
            if check_id_valid(self._id):
                return self._id
        raise StopIteration


def main():
    # assumed to be valid (digits only + 9 chars exactly + >= 100000000)
    id_num = int(input("Please supply ID number: "))

    # it will contain either a generator or an iterator, depends on the input
    gen_or_it = input("Generator or Iterator (gen/it?): ").lower()
    it = get_next_id(id_num) if gen_or_it == "gen" \
        else IDIterator(id_num) if "it" \
        else None

    # The generator and iterator generally work the same
    if isinstance(it, types.GeneratorType) or isinstance(it, IDIterator):
        try:
            for i in range(10):
                print(next(it))
        except StopIteration:
            print("Max ID (999999999) reached")
    else:
        print("Neither gen or it were chosen")


if __name__ == "__main__":
    main()
