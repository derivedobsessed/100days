from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    password_list = [choice(letters) for char in range(nr_letters)] + [choice(symbols) for char in range(nr_symbols)] + [choice(numbers) for char in range(nr_numbers)]
    shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='You have left some information blank')
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password")
logo = PhotoImage(file="logo.png")
window.config(padx=100, pady=50)
canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.create_image(100,  112, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", font=(FONT_NAME, 12, "bold"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=39)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="email", font=(FONT_NAME, 12, "bold"))
email_label.grid(column=0, row=2)
email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password", font=(FONT_NAME, 12, "bold"))
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3)

save_button = Button(text="Save", highlightthickness=0, width=40, command=save)
save_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
