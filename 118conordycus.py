import turtle as trtl

dragon = trtl.Turtle()


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
dragon.end_fill()


dragon.penup()
dragon.goto(215,175)
dragon.pendown()

dragon.circle(50,360,3)




wn = trtl.Screen()
wn.mainloop()
