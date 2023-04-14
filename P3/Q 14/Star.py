import turtle
# STAR
t = turtle.Turtle()
t.pencolor("black")
t.penup()
t.setposition(0, 0)
t.pendown()
for corner in range(1, 6):
    t.left(36+90+18)
    t.forward(200)
turtle.done()
