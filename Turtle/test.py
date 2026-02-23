import turtle

# Set up layar
screen = turtle.Screen()
screen.title("Turtle Movement with Keys")
screen.bgcolor("white")

# Buat turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# Fungsi untuk gerakan
def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(90)

def turn_right():
    t.right(90)

# Bind tombol keyboard
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Aktifkan listener
screen.listen()

# Tampilan
turtle.done()
