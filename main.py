import turtle

wn = turtle.Screen()
wn.title("Pong by Adi Cohen")
wn.bgcolor("black")
wn.tracer(0)
wn.setup(width=600, height=400)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=2, stretch_wid=4)
paddle_a.penup()
paddle_a.goto(-300.0, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=2, stretch_wid=4)
paddle_b.penup()
paddle_b.goto(300.0, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = -0.05

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 170)
pen.write("Player A:0  Player B:0", align="center", font=("Courier", 16, "normal"))

# Score
score_a = 0
score_b = 0

# function to move paddle a up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# function to move paddle a down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# function to move paddle b down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keybord input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 180:
        ball.sety(180)
        ball.dy *= -1

    if ball.ycor() < -180:
        ball.sety(-180)
        ball.dy *= -1
# right
    if ball.xcor() > 250:
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -250:
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # paddle ball collistions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(240)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-240)
        ball.dx *= -1



