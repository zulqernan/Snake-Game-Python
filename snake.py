import turtle
import time
import random

# Variables
score = 0
high_score = 0
segments = []

# 1. Screen Setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# 2. Snake Head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# 3. Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 4. Pen (Score likhne ke liye)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# 5. Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

        screen.listen()
# Arrow Keys
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# WSAD Keys
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

def reset_game():
    global score
    # 1. Screen par foran message likhein
    pen.goto(0, 0)
    pen.color("yellow") # Message ka color thora alag rakhein taaki nazar aaye
    pen.write("GAME OVER!", align="center", font=("Courier", 35, "bold"))
    
    # 2. Ye line zaroori hai: Screen ko update karein taaki text nazar aaye
    screen.update()
    
    # 3. Thori der wait karein taaki player message dekh sakay
    time.sleep(2)
    
    # 4. Ab game reset karein
    head.goto(0, 0)
    head.direction = "stop"
    
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    
    score = 0
    pen.color("white") # Wapas white color karein score ke liye
    update_score()
    
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    update_score()

def update_score():
    pen.clear()
    pen.goto(0, 260)
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# 6. Keyboard Bindings
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# 7. Main Loop
try:
    while True:
        screen.update()

        # Wall Collision
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            reset_game()

        # Food Collision
        if head.distance(food) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Score barhao
            score += 10
            if score > high_score:
                high_score = score
            update_score()

        # Move segments
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        # Body Collision
        for segment in segments:
            if segment.distance(head) < 20:
                reset_game()

        time.sleep(0.1)

except turtle.Terminator:
    pass