from turtle import Screen, Turtle, shape
import pandas

screen = Screen()
screen.title("US STATES")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)


data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    guess = screen.textinput(f"{len(guessed_states)}/50 States", "Can you guess another state?")
    guess.title()
    if guess in state_names:
        state_data = data[data.state == guess]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)
        guessed_states.append(guess)
    if guess == 'Exit':
        not_guessed = [state for state in state_names if state not in guessed_states]
        new_data = pandas.DataFrame(not_guessed)
        new_data .to_csv('not_guessed.csv')
    if len(guessed_states) ==50:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(-40, 0)
        t.write('Well done! You\'ve guessed all 50 states')


screen.exitonclick()
