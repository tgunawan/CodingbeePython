import turtle

wn = turtle.Screen()
wn.title("Conditional Turtle Example")

my_turtle = turtle.Turtle()

my_turtle.penup()
my_turtle.goto(-100, 0)
my_turtle.pendown()

for i in range(10):
    if i % 2 == 0:  # If 'i' is even
        my_turtle.forward(50)
        my_turtle.right(90)
    else:  # If 'i' is odd
        my_turtle.forward(100)
        my_turtle.left(90)

wn.mainloop()
