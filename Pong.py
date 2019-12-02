 #Author:	azmathias Stuperuser Ltd
 #Purpose:	A very simple console Pong solution, coded in the early stages of learning Python
 #TODO:		Develop another solution using OOP, add sounds, refine response times, create a movement class

    
import turtle
import winsound
 
wn = turtle.Screen()
wn.title("Pong by @stuperuser")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

#Score
score_a = 0
score_b = 0
 
	
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
	
#Paddle A
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) 

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) 

# Ball movement dX, dY
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 14, "normal"))

# Function to move paddle A, y coords
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)
	
def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)
	
	
# Function to move paddle B, y coords	
def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)
	
def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)
	
# call the function, keyboard binding on  Paddle A ("w", "s"), Paddle B ("Up", "Down")
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
	wn.update()
	
	# move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	#border checking (make it bounce) compare y coord, when it gets to a certain point, make it bounce
	if ball.ycor() > 287:
		ball.sety(287)
		ball.dy *= -1
		winsound.PlaySound("Bounce.wav&", winsound.SND_ASYNC)
		
	if ball.ycor() < -287:
		ball.sety(-287)
		ball.dy *= -1
		winsound.PlaySound("Bounce.wav&", winsound.SND_ASYNC)
		
		
	#border checking x coord, update score
	if ball.xcor() > 387:
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "normal"))
		
		
	#border checking x coord, update score
	if ball.xcor() < -387:
		ball.goto(0,0)
		ball.dx *= -1	
		score_b += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "normal"))
		

# paddle and ball collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
		ball.setx(340)
		ball.dx *= -1
		
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
		ball.setx(-340)
		ball.dx *= -1	
		
		
		
