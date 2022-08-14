#..........draw graph paper with python turtle......!
import turtle
#create turtle object
t=turtle.Turtle()
#set the pen speed
t.speed(10)
#Draw horizontal lines
for i in range(0,400,20):
      t.pencolor('lightgrey')
      t.penup()
      t.setpos(-200+i,-200)
      if i==0:
         t.left(90)
      t.pendown()
      t.forward(400)
      t.backward(400)
#Draw vertical lines
for i in range(0,400,20):
      t.pencolor('lightgrey')
      t.penup()
      t.setpos(-200,-200+i)
      if i==0:
         t.right(90)
      t.pendown()
      t.forward(400)
      t.backward(400)
t.penup()
#reposition
t.home()
t.pendown()
#change the pen color
t.pencolor('black')
t.backward(200)
t.forward(400)
t.backward(200)
t.left(90)
t.forward(200)
t.backward(400)
t.penup()
t.setpos(5,5)
t.pendown()
t.write(0)
t.penup()
t.setpos(190,5)
t.pendown()
t.write("x")
t.penup()
t.setpos(5,190)
t.pendown()
t.write("y")
t.penup()
t.setpos(0,-180)
t.pendown()
t.write("https://artificialintelligencestechnology.com/")
t.ht()
