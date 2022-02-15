# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# closer #s are to 255 -> probably white (remove)

import turtle as t
import random

t.colormode(255)
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

art = t.Turtle()
art.speed("fastest")
art.penup()

# set position to be at bottom left of screen
y = -250
art.setposition(-300, y)

art.hideturtle()


for _ in range(10):
    for i in range(10):
        art.dot(20, random.choice(color_list))
        art.penup()
        art.forward(50)
    y += 50
    art.penup()
    art.setposition(-300, y)


#art.dot(20)


# exit screen only on click
screen = t.Screen()
screen.exitonclick()