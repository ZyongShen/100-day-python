from turtle import Turtle

class Ball(Turtle):

    def __init__(self, shape, wid, len, color, start_x, start_y):
        super().__init__()
        super().shape(shape)
        super().shapesize(stretch_wid=wid, stretch_len=len)
        super().color(color)

        super().penup()
        super().hideturtle()
        super().setx(start_x)
        super().sety(start_y)
        super().showturtle()

        self.x_factor = 1
        self.y_factor = 1

    def bounce(self, invert_x, invert_y):
        if invert_x:
            self.x_factor *= -1
        if invert_y:
            self.y_factor *= -1

    def move(self):
        self.penup()
        x = self.xcor()+10*self.x_factor
        y = self.ycor()+10*self.y_factor
    
        
        self.goto(x, y)


