from turtle import *
s = Turtle()
s.speed(0)
s.up()
s.goto(0,100)
lst = ['red','blue','green','yellow','orange']
def pg1():
    for i in range (90):
        for j in range(5):
            s.color(lst[j])
            s.forward(100)
            s.right(30)
            s.forward(20)
            s.up()
            s.right(89)
            s.back(120)
            s.down()
pg1()
s.left(90)
s.forward(200)
s.write('HAPPY BIRTHDAY DEAR "TRIPTI" ', font=("Arial", 22,"normal"))
pg1()
s.left(90)
s.forward(590)
s.right(20)
pg1()
done()