import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor("pink")
my_turtle.speed(8)




def recursive_square(size, depth):
    if depth > 0:
        my_turtle.fd(size)
        my_turtle.left(90)
        my_turtle.fd(size)
        my_turtle.left(90)
        my_turtle.fd(size)
        my_turtle.left(90)
        my_turtle.fd(size)
        my_turtle.left(90)
        my_turtle.fd(size / 2)
        my_turtle.left(45)
        recursive_square((2 * ((size / 2) ** 2)) ** 0.5, depth - 1)

recursive_square(100, 15)


def recursive_random(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.left(30)
        my_turtle.fd(size / 2)
        recursive_random(x + size, y + size, size / 2, depth - 1)
        recursive_random(x + size, y - size, size / 2, depth - 1)

recursive_square(0, 0, 100, 15)



my_screen.exitonclick()
