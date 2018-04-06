import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor("pink")
my_turtle.speed(8)

def recursive_random(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.left(30)
        my_turtle.fd(size / 2)
        recursive_random((2 * ((size / 2) ** 2)) ** 0.5, depth - 1)

recursive_random(0, 0, 100, 15)



my_screen.exitonclick()