import turtle 

wind = turtle.Screen()    # intialize screen
wind.title("omar Bahloul")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

madrb1 = turtle.Turtle()  # madrab1
madrb1.speed(0)
madrb1.shape("square")
madrb1.color("blue")
madrb1.shapesize(stretch_wid=(5), stretch_len=(1))
madrb1.penup()
madrb1.goto(-360,0)

madrb2 = turtle.Turtle()   # madrab2
madrb2.speed(0)
madrb2.shape("square")
madrb2.color("red")
madrb2.shapesize(stretch_wid=(5), stretch_len=(1))
madrb2.penup()
madrb2.goto(360,0)

ball = turtle.Turtle()      # ball
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .2
ball.dy = .2

#score
scor1 =0
scor2 =0
scor=turtle.Turtle()
scor.speed(0)
scor.color("green")
scor.penup()
scor.hideturtle()
scor.goto(0,260)
scor.write("player 1: 0   player 2: 0",align="center",font=("Courier",25,"normal"))

def madrab_up ():
    y= madrb1.ycor()
    y+=20
    madrb1.sety(y)
    


def madrab_down ():
    y= madrb1.ycor()
    y-=20
    madrb1.sety(y)
    


def madrab_up2 ():
    y= madrb2.ycor()
    y+=20
    madrb2.sety(y)
    

def madrab_down2 ():
    y= madrb2.ycor()
    y-=20
    madrb2.sety(y)
    

wind.listen()
wind.onkeypress(madrab_up,"a")
wind.onkeypress(madrab_down2,"m")
wind.onkeypress(madrab_down,"z")
wind.onkeypress(madrab_up2,"k")


while True :
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*= -1
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*= -1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        scor1 +=1
        scor.clear()
        scor.write("player 1: {}   player 2: {}".format(scor1, scor2),align="center",font=("Courier",25,"normal"))
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        scor2 +=1
        scor.clear()
        scor.write("player 1: {}   player 2: {}".format(scor1, scor2),align="center",font=("Courier",25,"normal"))
        
    #  madrb2 and boll
    if (ball.xcor() >340 and ball.xcor() <350 and (ball.ycor() < madrb2.ycor() +50  and ball.ycor() > madrb2.ycor() -50)) :
        ball.setx(340)
        ball.dx *= -1
       
    
     #  madrb1 and boll
    if (ball.xcor() <-340 and ball.xcor() >-350 and (ball.ycor() < madrb1.ycor() +50  and ball.ycor() > madrb1.ycor() -50)) :
        ball.setx(-340)
        ball.dx *= -1
       
    
    
    
    
    
    
    
    
    
    
