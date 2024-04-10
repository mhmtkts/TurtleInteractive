import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def turn_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
    #turtle_instance.right(10)

def turn_left():
    #turtle_instance.left(10)
    turtle_instance.setheading(turtle_instance.heading()+10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=turn_right, key="Down")
drawing_board.onkey(fun=turn_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")
drawing_board.onkey(fun=turtle_pen_up, key="q")
drawing_board.onkey(fun=turtle_pen_down, key="w")








turtle.mainloop()