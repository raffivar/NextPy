class BigThing:
    def __init__(self, name="Really Big Thing"):
        self._name = name

    def size(self):
        return len(self._name)


class BigCat(BigThing):
    def __init__(self, name, size):
        BigThing.__init__(self, name)
        self._size = size

    def size(self):
        if self._size > 20:
            return "Very Fat"
        elif self._size > 15:
            return "Fat"
        else:
            return "OK"


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


main()
