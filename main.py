import turtle
from random import randint

#drawing board
drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle Graphic")

#variables

time = 20
score = 0


#score turtle


score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("blue")
score_turtle.penup()
score_turtle.goto(0, 285)


def score_turtle_func():
    score_turtle.clear()
    score_turtle.write(arg=f"Score : {score}", align="center", font=("Arial", 18, "normal"))
    drawing_board.ontimer(score_turtle_func, 750)

score_turtle_func()

#time turtle

time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.goto(0, 250)

def time_turtle_func():
    global time
    if time > 0:
        time_turtle.clear()
        time_turtle.write(arg=f"Time : {time}",align="center",font=("Arial",16,"normal"))
        time -=1
        drawing_board.ontimer(time_turtle_func, 1000)
    else:
        time_turtle.clear()
        time_turtle.write(arg="Game Over !!!", align="center", font=("Arial", 16, "normal"))
time_turtle_func()

#show hide turtle

show_hide_turtle = turtle.Turtle()
show_hide_turtle.hideturtle()
show_hide_turtle.shape("turtle")
show_hide_turtle.color("green")
show_hide_turtle.resizemode("user")
show_hide_turtle.turtlesize(2,2,4)
show_hide_turtle.penup()

def show_hide_turtle_func():

    if time > 0 :
        show_hide_turtle.hideturtle()
        show_hide_turtle.goto(randint(-225, 225), randint(-225, 225))
        show_hide_turtle.showturtle()
        drawing_board.ontimer(show_hide_turtle_func, 500)
    else:
        show_hide_turtle.hideturtle()

show_hide_turtle_func()

def score_plus(x, y):
    global score
    score += 1

show_hide_turtle.onclick(score_plus)




turtle.mainloop()

