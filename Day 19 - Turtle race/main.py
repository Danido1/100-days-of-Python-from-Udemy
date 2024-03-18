from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []

if user_bet:
    is_race_on = True
#Creacion de tortugas y colocarlas en su posición
for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(new_turtle)
# Crear el movimiento de las tortugas
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(1, 10)
        turtle.forward((random_distance))
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won! The {winning_color} turtle is the winner!")
            else:
                print(f"you have lost! The {winning_color} turtle is the winner!")

print(all_turtles)


#Cosas que se podrian mejorar:
#1-Solo dejar que el User escriba un color, si escribe otra cosa darle error y que lo vuelva a escribir.
#2- Un sistema de puntuacion del user
#3-Make the screen more bigger





screen.exitonclick()
