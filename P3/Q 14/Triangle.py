import turtle
# TRIANGLE
t = turtle.Turtle()
t.pencolor("black")
t.penup()
t.setposition(0, 0)
t.pendown()
for corner in range(1, 4):
    t.left(120)
    t.forward(200)
turtle.done()