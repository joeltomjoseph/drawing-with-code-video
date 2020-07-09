import turtle

'''This is the spiral design'''
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
turtle.speed("fastest")
turtle.tracer(0, 0)
for x in range(3600):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
turtle.update()
turtle.mainloop()

'''And this is the smiley face'''
#wn = turtle.Screen()
#smiles = turtle.Turtle()
#smiles.fillcolor("red")
#
#smiles.begin_fill()
#smiles.penup()
#smiles.goto(-75,150)
#smiles.pendown()
#smiles.circle(10)
#smiles.end_fill()     
#
#smiles.begin_fill()
#smiles.penup()
#smiles.goto(75,150)
#smiles.pendown()
#smiles.circle(10)
#smiles.end_fill()
#
#smiles.penup()
#smiles.goto(0,0)
#smiles.pendown()
#smiles.circle(100,90)
#
#smiles.penup()           
#smiles.setheading(180)
#smiles.goto(0,0)
#smiles.pendown()
#smiles.circle(-100,90)
#turtle.mainloop()