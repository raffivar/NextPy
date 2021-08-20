class Wolf:
    WolfAmount = 0

    def __init__(self, age, name="Octavio"):
        self._name = name
        self._age = age
        Wolf.WolfAmount += 1

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


def main():
    wolf1 = Wolf(28, "Karo")
    wolf2 = Wolf(33)
    print(wolf1.get_name())
    print(wolf2.get_name())
    wolf2.set_name("Fenris")
    print(wolf2.get_name())
    print("Animal amount:", Wolf.WolfAmount)


main()
