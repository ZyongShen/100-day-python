###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram as cg
import turtle
import random

def extract_colors():
    colors = cg.extract("image.jpg", 100)
    all_colors = []
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        all_colors.append((red, green, blue))
    print(len(all_colors))
    print(all_colors)
    return all_colors

def back_to_start(start_pos):
    t.penup()
    t.goto(start_pos[0], start_pos[1])
    t.left(90)
    t.forward(50)
    t.right(90)
    t.pendown()


if __name__ == "__main__":
    '''
    Requirement:
    10x10
    Size: 20
    Gap: 50
    '''
    turtle.colormode(255)
    turtle.setworldcoordinates(-1, -1, 600, 600)
    turtle.shape(None)

    template_colors = extract_colors()
    t = turtle.Turtle()

    # i: row, j: column
    for i in range(10):
        start_pos = t.pos()
        for j in range(10):
            t.dot(20, template_colors[random.randint(0, 34)])
            t.penup()
            t.forward(50)
            t.pendown()
        if i != 9:
            back_to_start(start_pos)

    turtle.done()