import turtle


t = turtle.Turtle()
t.speed(4)

#body
t.fillcolor('#13263a')
t.begin_fill()
t.penup()
t.setpos(0, 100)
t.pendown()
t.circle(50)
t.penup()
t.setpos(0, 0)
t.pendown()
t.circle(50)
t.penup()
t.setpos(0,-100)
t.pendown()
t.circle(50)
t.end_fill()


#legs(left)
t.penup()
t.setpos(-50,-75)
t.right(40)
t.pendown()
t.fillcolor('#13263a')
t.begin_fill()
t.forward(50)
t.right(50)
t.forward(20)
t.right(50)
t.forward(150)
t.right(150)
t.forward(150)
t.right(52)
t.forward(27)
t.end_fill()
#(right)
t.penup()
t.setpos(49, -75)
t.setheading(223)
t.pendown()
t.fillcolor('#13263a')
t.begin_fill()
t.forward(50)
t.left(50)
t.forward(20)
t.left(50)
t.forward(150)
t.left(150)
t.forward(150)
t.left(52)
t.forward(27)
t.end_fill()


#arms(L)
t.penup()
t.setpos(-54, 20)
t.setheading(90)
t.pendown()
t.fillcolor('#13263a')
t.begin_fill()
t.forward(50)
t.left(50)
t.forward(20)
t.left(50)
t.forward(150)
t.left(150)
t.forward(150)
t.left(52)
t.forward(27)
t.end_fill()
#(R)
t.penup()
t.setpos(54, 70)
t.setheading(270)
t.pendown()
t.fillcolor('#13263a')
t.begin_fill()
t.forward(50)
t.left(50)
t.forward(20)
t.left(50)
t.forward(150)
t.left(150)
t.forward(150)
t.left(52)
t.forward(27)
t.end_fill()

#headpiece(L)
t.penup()
t.setpos(-65, 160)
t.setheading(50)
t.pendown()
t.fillcolor('#13263a')
t.begin_fill()
t.forward(50)
t.left(50)
t.forward(20)
t.left(50)
t.forward(150)
t.left(150)
t.forward(150)
t.left(52)
t.forward(27)
t.end_fill()
#(R)
t.penup()
t.setpos(32, 195)
t.setheading(319)
t.pendown()
t.fillcolor('#13263a')
t.begin_fill()
t.forward(50)
t.left(50)
t.forward(20)
t.left(50)
t.forward(150)
t.left(150)
t.forward(150)
t.left(52)
t.forward(27)
t.end_fill()


#face
t.penup()
t.setpos(-38, 155)
t.pendown()
t.fillcolor('#ace600')
t.begin_fill()
t.circle(40)
t.end_fill()
#eyes
t.penup()
t.setpos(-34, 155)
t.pendown()
t.pencolor('black')
t.fillcolor('white')
t.begin_fill()
t.circle(15)
t.end_fill()

t.penup()
t.setpos(7, 155)
t.pendown()
t.pencolor('black')
t.fillcolor('white')
t.begin_fill()
t.circle(15)
t.end_fill()

#iris
t.penup()
t.setpos(11, 155)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(9)
t.end_fill()
#(L)
t.penup()
t.setpos(-28, 155)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(9)
t.end_fill()

#mouth
t.penup()
t.setpos(-9,125)
t.setheading(3)
t.pendown()
t.forward(30)
t.dot(8, 'white')


















t.hideturtle()








turtle.done()

