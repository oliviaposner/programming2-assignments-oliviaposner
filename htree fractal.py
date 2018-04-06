import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor("white")
my_turtle.speed(8)

x = 0
y = 0
size = 150

def recursive_h(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y) # center
        my_turtle.down()
        my_turtle.goto(x + size, y) # right middle
        my_turtle.goto(x + size, y + size) # top right corner
        my_turtle.goto(x + size, y - size) # bottom right corner
        my_turtle.goto(x + size, y) # right middle
        my_turtle.goto(x - size, y)
        my_turtle.goto(x - size, y + size)
        my_turtle.goto(x - size , y - size)
        recursive_h( x + size, y + size, size / 2, depth -1)
        recursive_h(x + size, y - size, size / 2, depth - 1)
        recursive_h(x - size, y + size , size / 2, depth - 1)
        recursive_h(x - size, y - size, size / 2, depth - 1)

recursive_h(0, 0 , 150, 4)



my_screen.exitonclick()



