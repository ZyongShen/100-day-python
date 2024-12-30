import turtle

if __name__=="__main__":
    t = turtle.Turtle()
    screen = turtle.Screen()

    def move_forward():
        t.forward(10)
    def move_backward():
        t.backward(10)
    def turn_counter_clockwise():
        t.left(10)
    def turn_clockwise():
        t.right(10)
    def clear():
        t.clear()

    screen.listen()
    screen.onkey(move_forward, "Up")
    screen.onkey(turn_counter_clockwise, "Left")
    screen.onkey(turn_clockwise, "Right")
    screen.onkey(clear, "c")
    screen.exitonclick()

    screen.mainloop()
    turtle.done()

