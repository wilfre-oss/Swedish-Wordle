from tkinter import Entry, Button, Label
from turtle import color
import settings
import util

class Interface:
    all = []

    def __init__(self, column, row):
        self.letter = None
        self.column = column
        self.row = row

        Interface.all.append(self)

    def create_letter(self, char, location):
        letter = Label(
            location,
            bg=settings.BG,
            fg=settings.FG,
            underline= True,
            font=(settings.FONT, 42),
            text= char
        )
        self.letter = letter
    

    @staticmethod
    def color_letter(color, cloumn, row):
        for interface in Interface.all:
            if interface.column == cloumn and interface.row == row:
                interface.letter.config(fg= color)

        