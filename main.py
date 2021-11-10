import turtle
import pandas as pd

right = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

note = turtle.Turtle()
note.hideturtle()
note.penup()
note.goto(-350, -280)
note.color("blue")
note.write("NOTE: Type 'exit' to exit the game", font=('Arial', 15, 'normal'))

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while right != 50:
    answer_state = screen.textinput(title=f"{right}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                state_data = data[data["state"] == state]
                t.goto(int(state_data.x), int(state_data.y))
                t.color("red")
                t.write(state_data.state.item())
        break

    if (answer_state in all_states) and (answer_state not in guessed_states):
        guessed_states.append(answer_state)
        right += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()
