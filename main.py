import turtle
import pandas

screen = turtle.Screen()
screen.title("United Stated Guess Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 52:
    answer_for_state = screen.textinput(f"{len(guessed_states)}/ 50 State Guessed", prompt="Guess a state").title()
    data_source = pandas.read_csv("50_states.csv")
    all_states = data_source.state.to_list()

    if answer_for_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_states.csv")
        break
    if answer_for_state in all_states:
        guessed_states.append(answer_for_state)
        dan = turtle.Turtle()
        dan.hideturtle()
        dan.penup()
        state_data = data_source[data_source.state == answer_for_state]
        dan.goto(int(state_data.x), int(state_data.y))
        dan.write(answer_for_state)


