# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 17-10-2019
# purpose: Lab 5 - GUI and card game using queue

from tkinter import *

# to use the queue FIFO
from queue import LifoQueue

import os

# to use the shuffle for shuffling the cards
from random import shuffle


class CardGame(Frame):

    # initialises the application
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # set up game logic here:
        # shuffle the cards before first use
        # create LIFO Queue to store cards
        self.card_stack = LifoQueue(maxsize=52)

        # store cards in a list
        self.cards = os.listdir("cards")
        self.cards.remove('Icon\r')
        self.cards.remove('closed_deck.gif')
        self.cards.remove('.idea')

        # For the first game, the cards are shuffled twice
        shuffle(self.cards)

        # variable for holding the score
        self.player_score = 0

        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        self.pack(expand=True)

        # shuffle cards
        shuffle(self.cards)

        # clear self.card_stack
        self.card_stack.queue.clear()

        # add cards into LIFO queue
        for next_card in self.cards:
            self.card_stack.put(next_card)

        first_card = self.card_stack.get()

        # reset score
        self.player_score = 0

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(self)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(self)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        self.open_card = Button(cards_frame)
        the_card = PhotoImage(file='cards/' + first_card)
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        self.closed_deck = Button(cards_frame, command=self.next_card)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        self.closed_deck.config(image=closed_card)
        self.closed_deck.grid(row=0, column=1, padx=2, pady=2)
        self.closed_deck.photo = closed_card

        self.done_button = Button(button_frame, text="I'm done!", command=self.finished)
        self.done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.init_window)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score), justify=LEFT)
        self.score_label.pack()

        self.update_score(first_card)

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    # method to show next card
    def next_card(self):
        if self.card_stack.empty():
            self.init_window()

        new_card = self.card_stack.get()
        the_card = PhotoImage(file='cards/' + new_card)
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        self.update_score(new_card)

    def finished(self):
        self.closed_deck['state'] = DISABLED
        self.done_button['state'] = DISABLED
        score_frame = LabelFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2)
        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score) + " Thanks for playing", justify=LEFT)
        self.score_label.pack()

    def update_score(self, current_card):
        score = str(current_card)[0]

        if score == 'j' or score == 'q' or score == 'k':
            self.player_score += int(10)
        else:
            self.player_score += int(score)

        self.score_label.config(text="Your score " + str(self.player_score))
        self.score_label.update_idletasks()

        if self.player_score == 21:
            self.win()
        elif self.player_score > 21:
            self.lose()

    def win(self):
        self.closed_deck['state'] = DISABLED
        self.done_button['state'] = DISABLED
        score_frame = LabelFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2)
        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score) + " You Win!", justify=LEFT)
        self.score_label.pack()

    def lose(self):
        self.closed_deck['state'] = DISABLED
        self.done_button['state'] = DISABLED
        score_frame = LabelFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2)
        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score) + " You lose!", justify=LEFT)
        self.score_label.pack()






        # def really(self):
    #     button_frame = LabelFrame(self)®
    #     button_frame.grid(row=0, column=1)
    #     done_button = Button(button_frame, text="Really?")
    #     done_button.grid(row=0, column=0, pady=12)


# object creation here:
root = Tk()
root.geometry("300x200")
root.title("Card Game")
app = CardGame(root)
root.mainloop()
