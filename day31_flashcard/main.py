BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
from tkinter import *
import pandas
from random import choice

timer = None

print('hi')
# ---------------------------- flip ------------------------------- #
def flip(english_word):
    back = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(image_on_canvas, image=back)
    canvas.itemconfig(language, text='French')
    translation_to_french = data.loc[data['English'] == english_word]['French'].values[0]
    canvas.itemconfig(word, text=translation_to_french)


def new_word():
    new_data = pandas.read_csv("data/my_french_words.csv")
    leftover_english_words = new_data.English.to_list()
    new_random_english_word = choice(leftover_english_words)
    random_english_word = new_random_english_word
    canvas.itemconfig(image_on_canvas, image=front)
    canvas.itemconfig(language, text='English')
    canvas.itemconfig(word, text=random_english_word)
# ---------------------------- right_reset ------------------------------- #
def right_reset(english_word):
    flip(english_word)
    # remove_word(english_word)
    global timer
    timer = window.after(1000, new_word())


# ---------------------------- wrong_reset ------------------------------- #
def wrong_reset(english_word):
    flip(english_word)
    global timer
    timer = window.after(1000, new_word())


# def remove_word(english_word):
#     row_to_remove = data.loc[data['English'] == english_word]
#     print(row_to_remove)
#     new_data = data.drop(index=row_to_remove.index)
#     print(new_data)
#     new_data.to_csv('data/my_french_words.csv')

# ---------------------------- UI SETUP ------------------------------- #
data = pandas.read_csv("data/my_french_words.csv")
english_words = data.English.to_list()
random_english_word = choice(english_words)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
image_on_canvas = canvas.create_image(400, 263, image=front)
language = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=random_english_word, font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


tick = PhotoImage(file="images/right.png")
right_button = Button(image=tick, highlightthickness=0, command=flip(random_english_word))
right_button.grid(row=1, column=0)

cross = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross, highlightthickness=0, command=wrong_reset(random_english_word))
wrong_button.grid(row=1, column=1)


window.mainloop()







