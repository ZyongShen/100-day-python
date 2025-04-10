from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, shape, wid, len, color, start_x):
        super().__init__()
        super().shape(shape)
        super().shapesize(stretch_wid=wid, stretch_len=len)
        super().color(color)

        super().penup()
        super().hideturtle()
        super().setx(start_x)
        super().showturtle()
        

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

