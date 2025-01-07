import turtle,time,random


__Pen = turtle.Pen()

__Pen.penup()
__Pen.goto(0, 200)
__Pen.write('Sumo Wresling AI', align="center", font = ('Arial', 30, 'normal'))
turtle.bgcolor("#33ccff")
turtle1 = turtle.Turtle()
turtle1.shape('turtle')
turtle1.penup()
turtle1.setheading(0)
turtle1.pencolor("#ff0000")
turtle1.fillcolor("#ff0000")
turtle1.goto((-20), 0)
turtle2 = turtle.Turtle()
turtle2.shape('turtle')
turtle2.penup()
turtle2.setheading(180)
turtle2.pencolor("#3366ff")
turtle2.fillcolor("#3333ff")
turtle2.goto(20, 0)

def lingkaran():
    __Pen.penup()
    __Pen.goto(0, (-200))
    __Pen.pensize(5)
    __Pen.speed(20)
    __Pen.pencolor("#000000")
    __Pen.fillcolor("#33cc00")
    __Pen.pendown()
    __Pen.begin_fill()
    __Pen.circle(200)
    __Pen.end_fill()
    __Pen.penup()
    __Pen.goto(0, 25)
    __Pen.setheading(270)
    __Pen.pendown()
    __Pen.forward(50)
    __Pen.penup()
    __Pen.goto(0, (130))
    __Pen.hideturtle()
    
lingkaran()

def push(num):
    turtle1.forward(num)
    turtle2.backward(num)

while True:
    turtle.update()
    push(random.randint(-10,10))
    if (turtle2.xcor() > 200):
        __Pen.write('Game Over\nPlayer 1 Win',align="center", font = ('Arial', 15, 'normal'))
        print('Player1 win')
        time.sleep(2)
        quit()
    elif (turtle1.xcor() < -200):
        __Pen.write('Game Over\nPlayer 2 Win',align="center", font = ('Arial', 15, 'normal'))
        print('Player2 win')
        time.sleep(2)
        quit()
    else:
        pass
turtle.done()
