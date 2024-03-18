import random
from tkinter import *
import pandas



BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# READ DATA
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

know_words = {}
unknow_words = {}
#print(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = to_learn[random.randint(0, 4900)]
    #current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_text, text=current_card["English"], font=("Arial", 60, "bold"), fill="black")
    canvas.itemconfig(old_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Español", fill="white")
    canvas.itemconfig(card_text, text=current_card["Spanish"], fill="white")
    canvas.itemconfig(old_image, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Window
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


# CREATE CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas 1º card
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
old_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic") )
card_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)




# BUTTONS
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(column=0, row=1)


next_card()































window.mainloop()



