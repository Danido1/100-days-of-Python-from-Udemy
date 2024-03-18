from turtle import Turtle



#This is in capital letters because is a constant. A constant mean that the data is never going to be modify
SNAKE_STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_DIRECTIONS = [90, 180, 270, 360]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]
        self.head.color = "Red"



#Create the three parts of the snake and append it to a list
    def create_snake(self):
        for position in SNAKE_STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def reset(self):
        for part in self.snake_parts:
            part.goto(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

    def extend(self):
        self.add_part(self.snake_parts[-1].position())


    #Make the snake to move and figure it out to the tail follow the head
    def snake_move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)




