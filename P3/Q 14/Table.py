import turtle
# TABLE
t = turtle.Turtle()
t.pencolor("black")
t.penup()
line_pos = 0
column_pos = 0
# Drawing lines
for _ in range(1, 7):
    t.setposition(0, line_pos)
    t.pendown()
    t.forward(100)
    t.penup()
    line_pos += 20
# Drawing columns
t.left(90)
for _ in range(1, 7):
    t.setposition(column_pos, 0)
    t.pendown()
    t.forward(100)
    t.penup()
    column_pos += 20
turtle.done()
