import turtle
import pandas
import csv


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle.shape(image)
# with open("50_states.csv") as states:
#     data = csv.reader(states)
#     list_states = []
#     for row in data:
#         if row[0] != "state":
#             list_states.append(row[0])
#     print(list_states)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50Guess the State",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        print(state_data.state)
        print(state_data.x)
        print(state_data.y)






#states_to_learn.csv












