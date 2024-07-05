#Anoushka Saha
#Flashcard App
#Day 31 Capstone
#July 5th, 2024

#Import
from tkinter import *
import pandas 
import random

to_learn = {}

#File not found error handling for first time code is run
try:
    data = pandas.read_csv("data/words_left.csv")
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")

current_card = {}

#Button functions
def x_clicked():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image = card_front)
    canvas.itemconfig(card_title, text =  "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    timer = window.after(3000, func = flip_card)

def check_clicked():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_left.csv", index = False)
    x_clicked()

#Flip card function
def flip_card():
    canvas.itemconfig(card_title, text =  "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_image, image = card_back)

#Window configurations
window = Tk()
window.minsize(width = 900, height = 650)
window.title("Flashcard App")
window.config(padx = 50, pady = 50, bg = "#B1DDC6")
timer = window.after(3000, func = flip_card)

#Question flashcard
canvas = Canvas(width = 800, height = 526)
canvas.config(bg = "#B1DDC6", highlightthickness = 0)
card_front = PhotoImage(file = "images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
card_image = canvas.create_image(400, 263, image = card_front)
card_title = canvas.create_text(400, 150, text = "French:", font = ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "word", font = ("Arial", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)

#Buttons
red_image = PhotoImage(file = "images/wrong.png")
dont_know = Button(image = red_image, highlightthickness = 0, command = x_clicked)
dont_know.grid(row = 1, column = 0)
green_image = PhotoImage(file = "images/right.png")
know = Button(image = green_image, highlightthickness = 0, command = check_clicked)
know.grid(row = 1, column = 1)

x_clicked()


window.mainloop()