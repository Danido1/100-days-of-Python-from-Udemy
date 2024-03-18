from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def move_up():
    tim.forward(10)

def move_down():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()




screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")


screen.exitonclick()