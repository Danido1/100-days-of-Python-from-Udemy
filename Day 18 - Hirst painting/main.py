
import turtle as t
import random

#import colorgram

# Get the colors from the image
#rgb_colors = []

#colors_from_image = colorgram.extract("200430102527-01-damien-hirst-severed-spots-super-169.jpg", 30)
#for color in colors_from_image:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r, g, b)
    #rgb_colors.append(new_color)

#print(rgb_colors)

tim = t.Turtle()
t.colormode((255))

colors_list = [(234, 251, 243), (197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68), (228, 160, 47), (243, 247, 253), (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11), (242, 34, 164), (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208), (11, 97, 62), (220, 160, 10), (18, 18, 43), (52, 211, 230), (11, 228, 239), (80, 73, 214), (238, 156, 217), (73, 212, 168), (81, 234, 202), (61, 233, 241), (5, 67, 42)]
number_of_dots = 100
#Image characteristics: Size of the dot: 20, Distance between dots: 50, numbers of dots in vertical and horizontal: 10

#Starting point
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225) # 225 se obtiene Restando 270(direccion sur) - 180(direccion oeste) = 90 , 90 / 2 = 45, 180 + 45 = 225.
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)  # turn left by 90 degree
        tim.forward(50)
        tim.setheading(180)  # turn left again
        tim.forward(500)  # move forward 10 dots X 50 paces
        tim.setheading(0)  # face right











screen = t.Screen()
screen.exitonclick()