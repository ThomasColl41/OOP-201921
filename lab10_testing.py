# lab for testing
# code largely from lab 2
# author: B. Schoen-Phelan
# date: 29-11-2019

class Types_and_Strings:

    def return_last_char(self, value):
        print("Originally entered: ", value)

        # return the last character
        return value[-1]

    def return_first_char(self, value):
        print("Originally entered: ", value)
        if not isinstance(value, str):
            raise TypeError("Wrong type, we need a string")
        else:
            return value[0]

    def return_first_three_char(self, value):
        print("Originally entered: ", value)
        return value[:2]

    def replace_all_a(self, value):
        print("Originally entered: ", value)
        return value.replace('a','-')

    def print_only_even(self, value):
        only_even = []
        for i in range(0, len(value) - 1, 2):
            only_even.append(value[i])

        return only_even

    def all_lower(self, value):
        return value # issue here, should show up in testing

