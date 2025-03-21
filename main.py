import turtle
import pandas

screen = turtle.Screen()
screen.title("TURKEY STATES GAME")
screen.bgcolor("pink")
screen.setup(width= 1400, height= 600)
image = "tr_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("tr_illeri.csv")
all_states = data.il.to_list()
guessed_states = []

while len(guessed_states) != len(all_states):
    answer_state = screen.textinput(title = f"{len(guessed_states)} /81 States Correct", prompt = "What's another state's name?").capitalize()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.il == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

screen.exitonclick()