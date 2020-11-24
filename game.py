import turtle as t
import random as rd 
import time as ti

t.bgcolor('brown')

cat = t.Turtle()
cat.shape('square')
cat.speed(0)
cat.penup()
cat.hideturtle()

pil = t.Turtle()
pshape = ((0,0),(18,6),(6,18))
t.register_shape('pil', pshape)
pil.shape('pil')
pil.color('yellow')
pil.penup()
pil.penup()
pil.hideturtle()
pil.speed()

gamestart = False
text = t.Turtle()
text.write('press space to start Chuze', align = 'center' , font=('Arial',18,'bold') )
text.hideturtle()


score = t.Turtle()
score.hideturtle()
score.speed(0)

def outside_window():
    leftw = -t.window_width() /2 
    rightw = t.window_width() /2 
    topw = t.window_width() /2 
    botw = -t.window_width() /2 
    (x,y) = cat.pos()
    out = x< leftw or x> rightw or y>topw or y<botw
    return out

def pilloc():
    pil.hideturtle()
    pil.setx(rd.randint(-200,200))
    pil.sety(rd.randint(-200,200))
    pil.showturtle()

def gover():
    cat.color('grey')
    pil.color('black')
    t.penup()
    t.write('game over press space to restart', align='center' , font=('Arial',18,'bold') )
    t.onkey(start,'space')

def scored(current_score):
    score.clear()
    score.penup()
    x = (t.window_width() /2 ) -50
    y = (t.window_height() /2 ) -50
    score.setpos(x,y)
    score.write(str(current_score), align='right', font=('Arial',18,'bold'))

ti.sleep(3)

def start():
    global gamestart
    if gamestart:
        return 
    gamestart = True
    score = 0
    text.clear()

    cat_speed = 2
    cat_len = 1
    cat.shapesize(1,cat_len,1)
    cat.showturtle()
    scored(score)
    pilloc()

    while True:
        cat.forward(cat_speed)
        if cat.distance(pil)< 20:
            pilloc()
            cat_len = cat_len + 1
            cat_speed = cat_speed + 1
            cat.shapesize(1,cat_len,1)
            score = score + 1
            scored(score)

        if outside_window():
            gover()
            break


def moveup():
    if cat.heading()== 0 or cat.heading() == 180:
        cat.setheading(90)
     
def movedown():
    if cat.heading()== 0 or cat.heading() == 180:
        cat.setheading(270)

     
def moveright():
    if cat.heading()== 90 or cat.heading() == 270:
        cat.setheading(0)

     
def moveleft():
    if cat.heading()== 90 or cat.heading() == 270:
        cat.setheading(180)

t.onkey(start,'space')
t.onkey(moveup,'Up')
t.onkey(movedown,'Down')
t.onkey(moveleft,'Left')
t.onkey(moveright,'Right')
t.onkey(start,'space')


t.listen()
t.mainloop()