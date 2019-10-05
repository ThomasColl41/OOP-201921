# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 29-09-2019
# purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    # def play_with_strings(self):
        # working with strings
        # message = input("Enter your noun: ")
        # print("Originally entered: " + message)

        # print only first and last of the sentence
        # print(message[0] + " " + message[-1])

        # use slice notation
        # print(message[0:1] + " " + message[-1:])

        # escaping a character
        # print("He said “that\'s fantastic”!")

        # find all a's in the input word and count how many there are
        # print(str(message.find('a')) + " " + str(message.count('a')))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        # print(message.replace('a','-'))

        # printing only characters at even index positions
        # print(message[0::2])


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: " + message)

        # hand the input string to a list and print it out
        print(message.split())

        # append a new element to the list and print
        list_message = message.split()

        list_message.append("appended message")

        print(list_message)

        # remove from the list in 3 ways
        del list_message[0]

        list_message.remove("appended message")

        list_message.pop(1)

        print(list_message)

        # check if the word cake is in your input list
        print("cake" in list_message)

        # reverse the items in the list and print
        list_message.reverse()

        print(list_message)

        # reverse the list with the slicing trick
        list_message[::-1]

        print(list_message)

        # print the list 3 times by using multiplication
        print(list_message*3)


tas = Types_and_Strings()
# tas.play_with_strings()
tas.play_with_lists()
