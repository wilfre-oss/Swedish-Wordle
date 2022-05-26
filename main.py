
from tkinter import *
import sys
import ctypes

from interface import Interface
import settings
import util
from game import Game

root = Tk()
root.config(bg=settings.BG)
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Woordle Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="gray10",
    width= settings.WIDTH,
    height= util.height(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="gray10",
    fg="navajo white",
    font=("Bahnschrift SemiBold", 48),
    text="Swedish Wordle"
)
game_title.place(x=util.width(20), y=util.height(5))

left_frame = Frame(
    root,
    bg="gray10",
    width= util.width(25),
    height= util.height(50)
)
left_frame.place(x=0, y=util.height(25))

center_frame = Frame(
    root,
    bg="gray10",
    width= util.width(75),
    height= util.height(50)
)
center_frame.place(x=util.width(37), y=util.height(20))

bottom_frame = Frame(
    root,
    bg="gray10",
    width= settings.WIDTH,
    height= util.height(25)
)
bottom_frame.place(x=0, y=util.height(75))

def submit_guess(event):
    try:
        game.check_guess(word_entry.get())
    except ValueError as inst:
        ctypes.windll.user32.MessageBoxW(0,
        str(inst),
        "Nope!",
        0)
    finally:
        word_entry.delete(0, 'end')

word_entry = Entry(
    bottom_frame,
    bg="navajo white",
    bd= "2",
    width=20,
    font=("Bahnschrift SemiBold", 20)
)
word_entry.place(x=util.width(30), y=util.height(5))
word_entry.bind('<Return>', submit_guess)

button = Button(
    bottom_frame,
    bg="navajo white",
    width= 20,
    height= 1,
    font=("Bahnschrift SemiBold", 20),
    text="Guess",
)
button.place(x=util.width(30), y=util.height(13))
button.bind('<Button-1>', submit_guess)

game = Game(center_frame)

root.mainloop()