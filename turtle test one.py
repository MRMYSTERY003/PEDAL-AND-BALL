import turtle as tu

wn = tu.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.title("game")
wn.tracer(0)

# left paddle
pl = tu.Turtle()
pl.shape("square")
pl.color("white")
pl.shapesize(stretch_wid=5, stretch_len=1)
pl.speed(0)
pl.penup()
pl.goto(-350, 0)

# paddle right
pr = tu.Turtle()
pr.shape("square")
pr.color("white")
pr.shapesize(stretch_wid=5, stretch_len=1)
pr.speed(0)
pr.penup()
pr.goto(350, 0)

# ball
b = tu.Turtle()
b.shape("circle")
b.color('white')
b.penup()
b.speed(0)
b.goto(0, 0)
bx = 0.4
by = 0.5


# score board
sa = 0
sb = 0
sc = tu.Turtle()
sc.color('white')
sc.penup()
sc.hideturtle()
sc.goto(0, 270)
sc.speed(0)
sc.write("PLAYER A : {}   PLAYER B : {}".format(sa, sb), align='center', font=("Algerian", 20, "normal"))


# movements

def pl_up():
    y = pl.ycor()
    y += 30
    pl.sety(y)


def pl_down():
    y = pl.ycor()
    y -= 30
    pl.sety(y)


def pr_up():
    y = pr.ycor()
    y += 30
    pr.sety(y)


def pr_down():
    y = pr.ycor()
    y -= 30
    pr.sety(y)


# listening in keyboard
wn.listen()
wn.onkeypress(pl_up, 'w')
wn.onkeypress(pl_down, 's')
wn.onkeypress(pr_up, 'Up')
wn.onkeypress(pr_down, 'Down')

while True:
    wn.update()
    b.setx(b.xcor() + bx)
    b.sety(b.ycor() + by)
    # movement in x axis
    if b.xcor() > 390:
        b.goto(0, 0)
        sa += 1
        sc.clear()
        sc.write("PLAYER A : {}   PLAYER B : {}".format(sa, sb), align='center', font=("Algerian", 20, "normal"))
    if b.xcor() < -390:
        b.goto(0, 0)
        sb += 1
        sc.clear()
        sc.write("PLAYER A : {}   PLAYER B : {}".format(sa, sb), align='center', font=("Algerian", 20, "normal"))
    # movement in y axis
    if b.ycor() > 290:
        by *= -1
    if b.ycor() < -290:
        by *= -1

    # collision checking
    if (350 > b.xcor() > 340) and (pr.ycor() + 50 > b.ycor() > pr.ycor() - 50):
        b.setx(340)
        bx *= -1

    if (-350 < b.xcor() < -340) and (pl.ycor() + 50 > b.ycor() > pl.ycor() - 50):
        bx *= -1
        b.setx(-340)


