import turtle   #turtle game module similar to pygame
import winsound       #communicate with os
import time     #importing time for delay

window = turtle.Screen()    
window.title("Pong by Brain Maharjan")      
window.bgcolor("white")     #background color
window.setup(width=800, height=600)     #screen size
window.tracer(0)        #stops window from updating

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()      # small turtle --> module name and capital Turtle --> class name
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)       #paddle position

#Paddle B
paddle_b = turtle.Turtle()      # small turtle --> module name and capital Turtle --> class name
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)       #paddle position

#Ball
ball = turtle.Turtle()   
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)     
ball.dx = 0.95     #dx means change in x i.e. delta x
ball.dy = 0.95

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 18, "normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor()     #Return y co-ordinates with the help of turtle game module
    y += 20     # Increment of ycor with 20
    paddle_a.sety(y) 

def paddle_a_down():
    y = paddle_a.ycor()     #Return y co-ordinates with the help of turtle game module
    y -= 20     # Decrement of ycor with 20
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor()     #Return y co-ordinates with the help of turtle game module
    y += 20     # Increment of ycor with 20
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor()     #Return y co-ordinates with the help of turtle game module
    y -= 20     # Decrement of ycor with 20
    paddle_b.sety(y)

#Keyboard binding
window.listen()     #Listens the keyboard input
window.onkeypress(paddle_a_up,"w")      #calls paddle_a_up function when w key is pressed in the keyboard
window.onkeypress(paddle_a_down,"s")    #calls paddle_a_down function when s key is pressed in the keyboard
window.onkeypress(paddle_b_up,"Up")     #calls paddle_b_up function when Up arrow key is pressed in the keyboard
window.onkeypress(paddle_b_down,"Down")     #calls paddle_b_down function when Down arrow key is pressed in the keyboard

#Main Game Loop
while True:
    window.update()     #evertime the loop runs, it updates the window
    
    #Move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1       #Reverse the direction of the ball
        winsound.PlaySound("Click Sound.wav", winsound.SND_ASYNC)
        
    #Collision of the ball at the bottom of the screen
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        winsound.PlaySound("Click Sound.wav", winsound.SND_ASYNC)

    #Ball reset
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1       #Reverse ball direction
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        winsound.PlaySound("Coin Sound.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        winsound.PlaySound("Coin Sound.wav", winsound.SND_ASYNC)

    #Paddle and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1 
        winsound.PlaySound("Click Sound.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Click Sound.wav", winsound.SND_ASYNC)

    if(score_a == 5):
        pen.clear()
        pen.write("Player A wins", align="center", font=("Courier", 18, "normal"))
        time.sleep(3)
        break
    if(score_b == 5):
        pen.clear()
        pen.write("Player B wins", align="center", font=("Courier", 18, "normal"))
        time.sleep(3)
        break