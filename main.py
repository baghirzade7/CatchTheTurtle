import turtle as ttl
import random

screen = ttl.Screen()
screen.bgcolor("orange")
screen.title("Catch the Turtle")
screen.screensize()
grid_size = 15
score_turtle= ttl.Turtle()
score=0
FONT = ("Arial,20,Bold")
turtle_list = []
game_over = False

countdown_turtle= ttl.Turtle()

def make_score_turtle():

    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.penup()
    top_height = screen.window_height() /2
    y = top_height * 0.9
    score_turtle.setposition(0,y)
    score_turtle.write("Score: 0", move=False, align="Center", font=FONT)

def make_turtle(x,y):
    t = ttl.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", move=False, align="Center", font=FONT)
        #print(x,y)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(3,3)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


def setup_turtles():
    x_cordinates = [-20,-10,0,10,20]
    y_cordinates = [-10,0,10,20]
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 400)

def countdown(time):
    global game_over
    countdown_turtle.color("blue")
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setposition(0, y - 25)
    countdown_turtle.clear()
    if time>0:
        countdown_turtle.clear()
        countdown_turtle.write("Time: {}".format(time), move=False, align="Center", font=FONT)
        screen.ontimer(lambda: countdown(time -1),1000)
    else:
        game_over =True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write("Game Over", move=False, align="Center", font=FONT)

def start_game():
    ttl.tracer(0)
    make_score_turtle()
    countdown(15)
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    ttl.tracer(1)

start_game()

ttl.mainloop()