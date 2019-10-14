import turtle as trtl
import random as rdn

dragon = trtl.Turtle()
fire = trtl.Turtle()

fire_list = ["red","orange","yellow"]
#makes the body
dragon.speed(5)
dragon.penup()
dragon.goto(-180,0)
dragon.pendown()

dragon.right(45)
dragon.pensize(5)
dragon.pencolor("red")

# makes the head
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

#makes the eyes
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
# makes the mouth and part of the eyes.
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

# This code makes the claws
dragon.penup() 
dragon.goto(-45,-45)
dragon.pendown()    
dragon.pencolor("red")
dragon.begin_fill()
dragon.fillcolor("red")
dragon.right(75)
dragon.circle(45,360,4)
dragon.penup() 
dragon.goto(-45,-105)
dragon.pendown()
dragon.circle(45,360,4)
dragon.goto(-35,-105)
dragon.circle(45,360,3)
dragon.end_fill()

dragon.penup()
dragon.goto(-135,-45)
dragon.pendown()
dragon.pencolor("red")
dragon.begin_fill()
dragon.fillcolor("red")
dragon.circle(45,360,4)
dragon.penup() 
dragon.goto(-135,-105)
dragon.pendown()
dragon.circle(45,360,4)
dragon.goto(-125,-105)
dragon.circle(45,360,3)
dragon.end_fill()

# makes the spikes on the body and tale.
dragon.penup()
dragon.goto(-75,75)
dragon.pendown()
dragon.begin_fill()
dragon.fillcolor("red")
dragon.circle(45,360,3)
dragon.penup()
dragon.goto(-115,75)
dragon.pendown()
dragon.circle(45,360,3)
dragon.penup()
dragon.goto(-155,75)
dragon.pendown()
dragon.circle(45,360,3)
dragon.penup()
dragon.goto(-195,75)
dragon.pendown()
dragon.circle(45,360,3)
dragon.penup()
dragon.goto(-235,55)
dragon.pendown()
dragon.circle(45,360,3)
dragon.end_fill()




fire.penup()
fire.goto(215,125)
fire.pendown()
fire.speed(0)

# makes the fire
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
    fire_2 += 1




wn = trtl.Screen()
wn.mainloop()
