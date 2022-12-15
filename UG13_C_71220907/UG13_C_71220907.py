import turtle

turtle.shape('square')

#Background
turtle.color('purple','pink')
turtle.begin_fill()
turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.end_fill()

#Angka 0
turtle.penup()
turtle.goto(30,30)
turtle.pendown()
turtle.left(90)
turtle.circle(30,180)
turtle.forward(60)
turtle.circle(30,180)
turtle.forward(60)

#Angka 9
turtle.penup()
turtle.goto(30,180)
turtle.pendown()
turtle.circle(30,360)
turtle.left(180)
turtle.forward(60)
turtle.left(180)
turtle.circle(30,-180)

#Angka 7
turtle.penup()
turtle.goto(-30,-90)
turtle.pendown()
turtle.left(90)
turtle.forward(60)
turtle.goto(-20,-210)

#Huruf G
turtle.penup()
turtle.goto(-120,60)
turtle.pendown()
turtle.left(180)
turtle.circle(60,180)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)

#Huruf T
turtle.penup()
turtle.goto(120,60)
turtle.pendown()
turtle.left(180)
turtle.forward(60)
turtle.penup()
turtle.goto(150,60)
turtle.pendown()
turtle.right(90)
turtle.forward(120)

turtle.hideturtle()
turtle.done()