import string


class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Username too short."


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Username contains illegal character."


class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Username too long."

    def get_password(self):
        return self._username


class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Password too short."


class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Password too long."


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password is missing a character"

    def get_password(self):
        return self._password


class Uppercase(PasswordMissingCharacter):
    def __str__(self):
        return super(Uppercase, self).__str__() + " (Upercase)"


class Lowercase(PasswordMissingCharacter):
    def __str__(self):
        return super(Lowercase, self).__str__() + " (Lowercase)"


class Digit(PasswordMissingCharacter):
    def __str__(self):
        return super(Digit, self).__str__() + " (Digit)"


class Special(PasswordMissingCharacter):
    def __str__(self):
        return super(Special, self).__str__() + " (Special)"


def is_valid_username(username):
    for char in username:
        if not char.isalpha() and not char.isdigit() and char != "_":
            return False
    return True


def is_valid_password(password):
    char_dict = {"upper": 0, "lower": 0, "digit": 0, "special": 0}

    for char in password:
        if char.isupper():
            char_dict["upper"] += 1
        elif char.islower():
            char_dict["lower"] += 1
        elif char.isnumeric():
            char_dict["digit"] += 1
        elif char in string.punctuation:
            char_dict["special"] += 1

    if char_dict["upper"] == 0:
        raise Uppercase(PasswordMissingCharacter)
    elif char_dict["lower"] == 0:
        raise Lowercase(PasswordMissingCharacter)
    if char_dict["digit"] == 0:
        raise Digit(PasswordMissingCharacter)
    if char_dict["special"] == 0:
        raise Special(PasswordMissingCharacter)

    return True


def check_input(username, password):
    try:
        if len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif not is_valid_username(username):
            raise UsernameContainsIllegalCharacter(username)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
        elif not is_valid_password(password):
            raise PasswordMissingCharacter(password)
    except Exception as e:
        print(e)
    else:
        print("OK")


def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


if __name__ == "__main__":
    main()
