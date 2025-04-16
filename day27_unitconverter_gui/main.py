from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)


dist_miles = Entry(width=5)
dist_miles.insert(END, string="0")
dist_miles.grid(column=2, row=1)


label_1 = Label(text="Miles")
label_1.grid(column=3, row=1)

label_2 = Label(text="is equal to")
label_2.grid(column=1, row=2)

dist_in_km = Label(text="0")
dist_in_km.grid(column=2, row=2)

label_4 = Label(text="KM")
label_4.grid(column=3, row=2)

def action():
    km = round(float(dist_miles.get())*1.609344)
    dist_in_km.config(text=f"{km}")

button = Button(text="Calculate", command=action)
button.grid(column=2, row=3)


window.mainloop()
