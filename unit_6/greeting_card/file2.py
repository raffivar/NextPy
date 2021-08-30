from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, sender_age=0):
        GreetingCard.__init__(self)
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print("Happy birthday!")
        print("{} is {} years old".format(self._sender, self._sender_age))
