import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")

text = turtle.Turtle()
text.color("black")
text.hideturtle()

image = "blank_states_img.gif"
screen.bgpic(image)

data = pd.read_csv("50_states.csv")

# Transform the state column to a list
states_list = data.state.to_list()
# Do a second list in lowercase
lowercase_states_list = [i.lower() for i in states_list]


x_series = data.set_index("state")["x"]
y_series = data.set_index("state")["y"]
# Transform the index to lowercase
x_series.index = x_series.index.str.lower()
y_series.index = y_series.index.str.lower()

#print(x_series)

game_is_on = True
correct_guess = []
while game_is_on:
    user_answer = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt= "What´s another state name?").lower()
    if user_answer in lowercase_states_list or user_answer in states_list:
        new_x = int(x_series.at[user_answer])
        new_y = int(y_series.at[user_answer])
        text.penup()
        text.goto(new_x, new_y)
        text.write(user_answer[0].upper() + user_answer[1:])
        correct_guess.append(user_answer)
        #print(f"x: {new_x} y: {new_y}")
        #print(correct_guess)
    elif len(correct_guess) == 50:
        game_is_on = False
    elif user_answer == "exit":
        state_not_guess = [state for state in lowercase_states_list if state not in correct_guess]
        new_data = pd.DataFrame(state_not_guess)
        new_data.to_csv("states_to_learn.csv")
        #print(state_not_guess)
        break
    else:
        text.penup()
        text.goto(-100, 250)
        text.write("That is not a correct answer", font="arial")

# States to learn.csv





#turtle.mainloop()

