from turtle import *
s = Turtle()
w = Screen()

w.title('INDIAN FLAG')
s.shape('turtle')
s.speed(1)

s.up()
s.goto(-200,230)
s.down()
s.color('orange')
s.begin_fill()
s.forward(230)
s.right(90)
s.forward(45)
s.right(90)
s.forward(230)
s.right(90)
s.end_fill()
s.pencolor('green')
#s.color()
#s.begin_fill()
s.forward(45)
s.back(90)
s.right(90)
s.forward(230)
s.left(90)
s.forward(45)
s.back(45)
#s.end_fill()
s.left(90)
s.forward(115)
s.color('blue')
s.pencolor()
s.circle(-22)
s.right(90)
s.forward(25)
s.circle(-2)
s.left(165)
for i in range(1,24):
    s.forward(21)
    s.back(21)
    s.right(15)
s.forward(25)
s.pencolor('green')
s.left(90)
s.forward(115)
s.right(90)
s.color("green")
s.begin_fill()
s.forward(45)
s.right(90)
s.forward(230)
s.right(90)
s.forward(45)
s.end_fill()
s.back(45)
s.pencolor('black')
s.left(180)

s.color('black')
s.begin_fill()
s.forward(300)
s.right(90)
s.forward(15)
s.right(90)
s.forward(434)
s.right(90)
s.forward(15)
s.end_fill()
s.back(15)
s.right(90)

s.forward(434)
s.color('gray')
s.begin_fill()
s.right(90)
s.forward(100)
s.back(240)
s.left(90)
s.forward(40)
s.right(90)
s.forward(250)
s.right(90)
s.forward(40)
s.end_fill()
s.back(20)
s.color('gray')
s.begin_fill()
s.left(90)
s.forward(30)
s.left(90)
s.forward(35)
s.left(90)
s.forward(320)
s.left(90)
s.forward(35)
s.left(90)
s.forward(40)
s.end_fill()
s.up()
s.back(90)
s.down()
s.pencolor('#ff8000')
s.write('Vishnu Sahani ', font=("Arial", 34,"normal"))
s.up()
s.goto(-160,20)
s.down()
s.pencolor('#ff8000')

s.write('INDIAN ARMY ', font=("Arial", 54,"normal"))
#s.write('Vishnu Sanahi', font=("Arial", 44,"normal"))
s.pencolor('red')

s.back(450)

done()