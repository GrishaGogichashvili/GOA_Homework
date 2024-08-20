from turtle import *

width (7)

speed(0)

for i in range (4):
  forward(250)
  left(90)

penup()
goto(-350, 0)
pendown()

for i in range (4):
  forward(250)
  left(90)

penup()
goto(0,-350)
pendown()

for i in range (4):
  forward(250)
  left(90)

penup()
goto(-350,-350)
pendown()

for i in range (4):
  forward(250)
  left(90)

exitonclick()