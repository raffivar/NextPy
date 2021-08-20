class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def birthday(self):
        self.age += 1


def main():
    wolf1 = Wolf("Raffi", 33)
    wolf2 = Wolf("Karo", 28)
    wolf2.birthday()
    print(wolf1.get_age())
    print(wolf2.get_age())


main()


