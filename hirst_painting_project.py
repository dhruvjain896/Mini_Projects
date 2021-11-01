import colorgram
import turtle as t
import random

t.colormode(255)

colors = colorgram.extract('hirst_painting.jpg', 100)
list_of_colors = []
for color in colors:
    list_of_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

tim = t.Turtle()

tim.speed("fastest")

tim.penup()
tim.hideturtle()
tim.right(180)
tim.forward(300)
tim.left(90)
tim.forward(300)
tim.left(90)


for i in range(10):
    for j in range(10):
        tim.color()
        tim.dot(20, random.choice(list_of_colors))
        tim.forward(50)
    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)


screen = t.Screen()
screen.exitonclick()