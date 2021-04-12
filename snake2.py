#imports
import turtle
import time
import random

#image
apple = "image/tako.gif"
shark = "image/shark.gif"
bloop = "image/bloop.gif"

#scores
score = 0
high_score = 0

#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)

#Head of the snake
wn = turtle.Screen()
wn.bgpic("image/seabackground.gif")
wn.register_shape(apple)
wn.register_shape(shark)
wn.register_shape(bloop)
game = wn.numinput("NIM", "1.Facile 2.Moyen 3.Difficile")
if(game == 1):
    delay = 0.1
elif(game == 2):
    delay = 0.06
elif(game == 3):
    delay = 0.03
else:
    delay = 0.02

wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape(shark)

head.penup()
head.goto(0,0)
head.direction = "stop"


#snake food
food= turtle.Turtle()
food.speed(0)
food.shape(apple)
food.penup()
food.goto(0,100)

segments = []

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

is_paused = False
def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
def restart():

        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments of body
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #clear the segments
        segments.clear()

        score = 0

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "z")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "q")
wn.onkeypress(go_right, "d")
wn.onkeypress(toggle_pause, "p")
wn.onkeyrelease(toggle_pause, "p")




while (True):
    if (is_paused == True):
        head.fd(1)
        head.lt(1)
        
    else:
        wn.update()
        
        #check collision with border area
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            if(game == 1):
                delay = 0.1
            elif(game == 2):
                delay = 0.06
            elif(game == 3):
                delay = 0.03
            else:
                    delay = 0.02
            score = 0
            restart()


        #check collision with food
        if head.distance(food) <20:
            # move the food to random place
            x = random.randint(-290,290)
            y = random.randint(-290,290)
            food.goto(x,y)

            #add a new segment to the head
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape(bloop)
            new_segment.color("black")
            new_segment.penup()
            segments.append(new_segment)

            #shorten the delay
            delay -= 0.001
            #increase the score
            score += 10

            if score > high_score:
                high_score = score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 

        #move the segments in reverse order
        for index in range(len(segments)-1,0,-1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)
        #move segment 0 to head
        if len(segments)>0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()

        #check for collision with body
        for segment in segments:
            if segment.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                #hide segments
                for segment in segments:
                    segment.goto(1000,1000)
                segments.clear()
                score = 0
                if(game == 1):
                    delay = 0.1
                elif(game == 2):
                    delay = 0.06
                elif(game == 3):
                    delay = 0.03
                else:
                    delay = 0.02

                #update the score     
                sc.clear()
                sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
        #on keypress r
        if(wn.onkeypress(restart, "r")):
            score = 0
            if(game == 1):
                delay = 0.1
            elif(game == 2):
                delay = 0.06
            elif(game == 3):
                delay = 0.03
            else:
                delay = 0.02
            
            
            restart()
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))

        
        


        time.sleep(delay)


    


