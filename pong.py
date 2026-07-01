import turtle

# Setup
wn = turtle.Screen()
wn.title("PONG by Daniel (@zendayasbrother)")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
winning_score = 7  # Set to None if you don't want a game over condition

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5  # Adjusted for gradual speed increase
ball.dy = 1.5

# Pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle movement functions with boundary checks
def paddle_a_up():
    if paddle_a.ycor() < 250:  # Upper limit
        paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    if paddle_a.ycor() > -240:  # Lower limit
        paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    if paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    if paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
def game_loop():
    global score_a, score_b, ball

    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision (Top & Bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Scoring & Reset Ball
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1.1  # Speed up ball slightly

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1.1  # Speed up ball slightly

    # Check if a player wins
    if winning_score and (score_a >= winning_score or score_b >= winning_score):
        pen.goto(0, 0)
        winner = "Player A" if score_a >= winning_score else "Player B"
        pen.write(f"{winner} Wins!", align="center", font=("Courier", 36, "bold"))
        return  # Stops game loop

    wn.ontimer(game_loop, 10)  # Runs game loop continuously

# Start game loop
game_loop()
wn.mainloop()
