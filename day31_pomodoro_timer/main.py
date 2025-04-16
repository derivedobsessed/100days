from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ticks_string = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global ticks_string
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    reps = 0
    ticks_string = ""
    ticks.config(text=ticks_string)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    global ticks_string
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        ticks.config(text=ticks_string)
        timer_label.config(text="Long Break", fg=PINK)
        count_down(5)
    elif reps % 2 == 1:
        timer_label.config(text="Focus Time", fg=GREEN)
        count_down(3)
        ticks_string = ticks_string + "✔"
    else:
        ticks.config(text=ticks_string)
        timer_label.config(text="Short Break", fg=RED)
        count_down(2)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    time = f'{count_min}:' + f'{count_sec}'
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
tomato_image = PhotoImage(file="tomato.png")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

ticks = Label(text=ticks_string, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
ticks.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,  112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()
