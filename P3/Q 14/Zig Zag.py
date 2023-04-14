import turtle
# ZIG ZAG
t = turtle.Turtle()
t.pencolor("black")
t.penup()
t.setposition(0, 0)
t.pendown()
t.left(65)
turn = -1
for corner in range(1, 9):
    turn = -turn
    t.forward(200)
    t.right(150 * turn)
turtle.done()
