class UnderAgeException(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return "Guest is underage."

    def get_age(self):
        return self._age


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAgeException(age)
        else:
            print("You should send an invite to " + name)
    except UnderAgeException as e:
        print("{}\nGuest is {} years old, "
              "will be able to attend to the party in {} year(s).".format(e, e.get_age(), (18 - e.get_age())))


def main():
    send_invitation("Dana", 17)


if __name__ == "__main__":
    main()
