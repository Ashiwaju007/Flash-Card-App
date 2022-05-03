from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')

new_word = data.to_dict(orient="records")


# ---------------------------- READ DATA ------------------------------- #
def next_card():
    global word, flip_timer, new_word
    window.after_cancel(flip_timer)
    word = random.choice(new_word)
    canvas.itemconfig(language_text, text=f"French", fill="black")
    canvas.itemconfig(word_text, text=f"{word['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(language_text, text=f"English", fill="white")
    canvas.itemconfig(word_text, text=f"{word['English']}", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


# ---------------------------- SAVE LIST ------------------------------- #
def save_list():
    new_word.remove(word)
    data = pandas.DataFrame(new_word)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=850, height=550, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(425, 275, image=card_front_img)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=1, row=2)
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=save_list)
right_button.grid(column=2, row=2)


next_card()


window.mainloop()

