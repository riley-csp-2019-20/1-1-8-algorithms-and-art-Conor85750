import turtle as trtl
import random as rdn

dragon = trtl.Turtle()
fire = trtl.Turtle()

fire_list = ["red","orange","yellow"]

dragon.speed(5)
dragon.penup()
dragon.goto(-180,0)
dragon.pendown()

dragon.right(45)
dragon.pensize(5)
dragon.pencolor("red")


dragon.begin_fill()
dragon.fillcolor("red")
dragon.circle(90,360,4)
dragon.goto(-55,0)
dragon.circle(90,360,4)
dragon.goto(45,90)
dragon.circle(120,360,4)



dragon.goto(-180,0)
dragon.left(75)
dragon.circle(75,360,3)
dragon.end_fill()


dragon.penup()
dragon.goto(135,210)
dragon.pendown()
dragon.begin_fill()
dragon.fillcolor("black")
dragon.pencolor("black")
dragon.circle(20)
dragon.penup()
dragon.goto(190,210)
dragon.pendown()
dragon.circle(20)
dragon.end_fill()

dragon.begin_fill()
dragon.fillcolor("white")
dragon.penup()
dragon.goto(135,210)
dragon.pendown()
dragon.circle(10)
dragon.penup()
dragon.goto(190,210)
dragon.pendown()
dragon.circle(10)
dragon.penup()
dragon.goto(215,115)
dragon.pendown()

dragon.circle(50,360,3)
dragon.end_fill()


fire.penup()
fire.goto(215,125)
fire.pendown()
fire.speed(0)


fire_1 = 0
fire_2 = 0
while fire_1 < 25:
    fire.pencolor(rdn.choice(fire_list))
    fire.pensize(5)
    fire.circle(25)
    fire.forward(10)
    fire_1 += 1
fire.penup()
fire.goto(215,145)
fire.pendown()
while fire_2 < 25:
    fire.pencolor(rdn.choice(fire_list))
    fire.pensize(5)
    fire.circle(25)
    fire.forward(10)
    fire_1 += 1
    
    

   





wn = trtl.Screen()
wn.mainloop()
