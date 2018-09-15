#! /usr/bin/python3

# This program creates a guessing game with a GUI using tkinter.

from tkinter import *
import random

class GuessingGame:
    GUESS_RESULTS = ["You Got it Correct!",
                    "Wrong. Lower.", 'Wrong. Higher.']

    def __init__(self, root):
        self.guess = 0
        self.number = 0
        self.root = root
        root.title("The Guessing Game")

        """ Top row, which indicates results.
            Changes are items in GUESS RESULTS
            attribute. """
        self.result_label_text = StringVar()
        self.result_label_text.set("")
        self.result_label = Label(root, textvariable=self.result_label_text)
        self.result_label.grid(row=0, columnspan=3, column=0, sticky=W+E)

        self.guess_label = Label(root, text="Enter Your Guess Below:")
        self.guess_label.grid(columnspan=1, row=1, column=0, sticky=W)

        self.show_last_guess = Label(root, text="Last Guess:")
        self.show_last_guess.grid(row=1, column=1, sticky=E)

        """ This displays the last guess the player
            made. """
        self.last_guess_text = IntVar()
        self.last_guess_text.set(self.guess)
        self.last_guess = Label(root, textvariable=self.last_guess_text)
        self.last_guess.grid(row=1, column=2)

        """ Input field, which clears after
            input is entered. """
        entryfield = root.register(self.validate)

        self.input = Entry(root, validate="key", validatecommand=(entryfield, "%P"))
        self.input.grid(row=2, column=0, columnspan=3, sticky=W+E)

        """ Buttons to select range from which
            to make a guess. Calls on select_num()
            based on range. """
        self.ten_label = Label(root, text="From 1 to 10:")
        self.ten_label.grid(row=3, column=0)
        self.ten = Button(root, text="Click To Start", command=lambda : self.select_num(10))
        self.ten.grid(row=3, column=1)

        self.fifty_label = Label(root, text="From 1 to 50:")
        self.fifty_label.grid(row=4, column=0)
        self.fifty = Button(root, text="Click To Start", command=lambda : self.select_num(50))
        self.fifty.grid(row=4, column=1)

        self.hundred_label = Label(root, text="From 1 to 100:")
        self.hundred_label.grid(row=5, column=0)
        self.hundred = Button(root, text="Click To Start", command=lambda : self.select_num(100))
        self.hundred.grid(row=5, column=1)

        """ This button checks if input is correct by calling
            the check_guess() function. """
        self.check = Button(root, text="E\nN\nT\nE\nR", command=self.check_guess)
        self.check.grid(column=2, rowspan=3, row=3)

        self.close = Button(root, text="Quit", command=self.root.quit)
        self.close.grid(row=6, columnspan=3, column=0, sticky=W+E)

    def validate(self, text):
        """ Ensures that correct, integer based input
            is provided to the entry field. """
        if not text:
            self.guess = 0
            return True
        else:
            try:
                self.guess = int(text)
                return True
            except ValueError:
                return False

    def select_num(self, guess_range):
        """ Selects random number within range
            of selected button. Also sets
            the last guess label to be displayed. """
        self.number = random.randint(1, guess_range)

    def check_guess(self):
        self.last_guess_text.set(self.guess)

        if self.number == 0:
            self.result_label_text.set("Select A Range.")
        elif self.guess == self.number:
            self.result_label_text.set(self.GUESS_RESULTS[0])
        elif self.guess > self.number:
            self.result_label_text.set(self.GUESS_RESULTS[1])
        else:
            self.result_label_text.set(self.GUESS_RESULTS[2])

        self.input.delete(0, END)

def main():
    root = Tk()

    app = GuessingGame(root)

    root.mainloop()

if __name__ == "__main__":
    main()
