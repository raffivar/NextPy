def check_id_valid(id_number):
    """Checks if an ID number is valid
    :param id_number: represents an ID number
    :type id_number: int
    :return: True if the id_number is valid, false otherwise
    :rtype: bool"""
    id_list = list(map(int, (str(id_number))))
    id_mult = list(map(lambda item: 2 ** (item[0] % 2) * item[1], enumerate(id_list)))
    id_united = list(map(lambda n: (n % 10 + n // 10) if n > 0 else n, list(id_mult)))
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
    id_num = int(input("Please supply ID number: "))
    gen_or_it = input("Generator or Iterator (gen/it?): ").lower()

    if gen_or_it == "gen":
        fun = get_next_id(id_num)
        try:
            for i in range(10):
                print(next(fun))
        except StopIteration:
            print("Max ID (999999999) reached")
    elif gen_or_it == "it":
        it = IDIterator(id_num)
        try:
            for i in range(10):
                print(next(it))
        except StopIteration:
            print("Max ID (999999999) reached")


if __name__ == "__main__":
    main()
