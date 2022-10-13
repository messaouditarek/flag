from turtle import *

bgcolor('red')

penup()

goto(0,-90)

pendown()

color('white')

begin_fill()

circle(90)

end_fill()



penup()

goto(0,-60)

pendown()

color('red')

begin_fill()

circle(60)

end_fill()



penup()

goto(18,-54)

pendown()

color('white')

begin_fill()

circle(54)

end_fill()



penup()

goto(0,-10)

pendown()



AF=25

a=180-180/5

color('red')

begin_fill()

for i in range(5):

    forward(AF)

    right(a-360/5)

    forward(AF)

    left(a)

end_fill() 

hideturtle()
