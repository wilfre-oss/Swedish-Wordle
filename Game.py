
import ctypes
import random
import json
from tkinter import *
from interface import Interface

class Game:
    location = None
    def __init__(self, location):
        with open('svenska-ord.json', encoding="utf-8") as word_file:
            self.word_list = set(word_file.read().split())
            self.word_list = [''.join(c for c in word if c not in '":,ë').lower()
                            for word in self.word_list if len(word) == 8]
        self.correct_word = random.choice(self.word_list)
        print(self.correct_word)
        self.guess_count = 0
        Game.location = location

    def check_guess(self, guess):

        if len(guess) != 5:
            raise ValueError("The word must be 5 characters long.")
        if guess not in self.word_list:
            raise ValueError("Not a word in the list.")
        self.guess_count += 1
        correct_letters = 0
        print(self.correct_word)

        for i,letter in enumerate(guess):
            self.create_letters(i, letter)
            if letter == self.correct_word[i]:
                correct_letters += 1
                Interface.color_letter("green", i, self.guess_count)
            elif letter in self.correct_word:
                Interface.color_letter("yellow", i, self.guess_count)
        
        if correct_letters == 5:
            ctypes.windll.user32.MessageBoxW(0,
            "Congratulations, you win!",
            "You Win!",
            0)
        elif self.guess_count == 6:
            ctypes.windll.user32.MessageBoxW(0,
            "You have used all guess attempts",
            "Game Over",
            0)
        
           

    def create_letters(self, x, char):
        letter = Interface(x, self.guess_count)
        letter.create_letter(char, Game.location)
        letter.letter.grid(
        column= x, row=self.guess_count

    
)