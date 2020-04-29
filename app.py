import turtle

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
scoreA = 0
scoreB = 0

# create pattle 1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape('square')
p1.color('white')
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350, 0)

# create paddle 2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape('square')
p2.color('white')
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=('Courier', 24, 'normal'))

def paddleAUp():
    y = p1.ycor() 
    if y < 300:
        y += 20
    p1.sety(y)

def paddleADown():
    y = p1.ycor()
    if y > -300:
        y -= 20
    p1.sety(y)

def paddleBUp():
    y = p2.ycor() 
    if y < 300:
        y += 20
    p2.sety(y)

def paddleBDown():
    y = p2.ycor()
    if y > -300:
        y -= 20
    p2.sety(y)

wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleBDown, "Down")

#main game loop
while True:
    wn.update()

    #move ball - if it moves out of screen, wrap around like a torus - move to 600 - ycor()
    ball.setpos(ball.xcor() + ball.dx, ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=('Courier', 24, 'normal'))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=('Courier', 24, 'normal'))


    #check for collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < p2.ycor() + 50 and ball.ycor() > p2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

