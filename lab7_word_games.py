# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 07-11-2019
# purpose: Lab 7 - Word Games

class WordGames:
    def __init__(self):
        self.mywords = input("Please enter a word or sentence: ")
        self.word_play()

    def word_play(self):
        print("User input was: "+self.mywords)

class WordDupli(WordGames):
    pass

class WordScramble(WordGames):
    pass

wg = WordGames()