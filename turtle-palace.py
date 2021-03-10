import turtle
turtle.setup(800, 800)
turtle.bgcolor('light sky blue')
turtle.home()
turtle.shape("turtle")


def square(side_horiz, side_vert, pencol, fillcol):
    angle = 90
    turtle.color(pencol, fillcol)
    turtle.begin_fill()

    for side in range(2):
        turtle.forward(side_horiz)
        turtle.right(angle)
        turtle.forward(side_vert)
        turtle.right(angle)

    turtle.end_fill()


def triangle(side_length, pencol, fillcol):
    angle = 120
    turtle.color(pencol, fillcol)
    turtle.begin_fill()

    for side in range(3):
        turtle.forward(side_length)
        turtle.left(angle)

    turtle.end_fill()


def tri_flag(side_length1, side_length2, pencol, fillcol):
    # angle1 = 10
    angle2 = 20
    angle3 = 80
    turtle.color(pencol, fillcol)
    turtle.begin_fill()

    turtle.left(angle2)
    turtle.forward(side_length1)
    turtle.left(angle2)
    turtle.forward(side_length1)
    turtle.left(angle3)
    turtle.forward(side_length2)

    turtle.end_fill()


def circle(radius, pencol, fillcol):
    turtle.color(pencol, fillcol)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def moveto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def battlements(x, y):

    for battlement in range(6):
        moveto(x, y)
        square(25, 25, 'black', 'gainsboro')
        x += 50


moveto(-150, 100)
square(300, 200, 'black', 'gainsboro')  # main block
moveto(-250, 200)
square(100, 300, 'black', 'white')  # left tower
triangle(100, 'black', 'orange red')  # left tower roof
moveto(150, 200)
square(100, 300, 'black', 'white')  # right tower
triangle(100, 'black', 'orange red')  # right tower roof
moveto(-75, 225)
square(150, 125, 'black', 'white')  # tower
triangle(150, 'black', 'orange red')  # middle tower roof
moveto(-50, 0)
square(100, 100, 'black', 'saddle brown')  # middle door
moveto(-220, 180)
square(40, 40, 'black', 'light cyan')  # left window
moveto(180, 180)
square(40, 40, 'black', 'light cyan')  # right window
moveto(-50, 200)
square(100, 50, 'black', 'light cyan')  # middle window

# battlements
battlements(-150, 125)

# lawn
moveto(-400, -100)
square(800, 300, 'lime green', 'lime green')

# flower 1 - petal
moveto(-100, -150)
turtle.dot(10, "yellow")
# petal
moveto(-105, -145)
turtle.dot(10, "yellow")
# petal
moveto(-100, -140)
turtle.dot(10, "yellow")
# petal
moveto(-95, -145)
turtle.dot(10, "yellow")
# flower-middle
moveto(-100, -145)
turtle.dot(6, "orange")

# flower 2 - petal
moveto(-130, -170)
turtle.dot(10, "yellow")
# petal
moveto(-135, -165)
turtle.dot(10, "yellow")
# petal
moveto(-130, -160)
turtle.dot(10, "yellow")
# petal
moveto(-125, -165)
turtle.dot(10, "yellow")
# flower-middle
moveto(-130, -165)
turtle.dot(6, "orange")

# flower 3 - petal
moveto(-110, -190)
turtle.dot(10, "yellow")
# petal
moveto(-115, -185)
turtle.dot(10, "yellow")
# petal
moveto(-110, -180)
turtle.dot(10, "yellow")
# petal
moveto(-105, -185)
turtle.dot(10, "yellow")
# flower-middle
moveto(-110, -185)
turtle.dot(6, "orange")

# left wavy flag
moveto(-200, 290)
tri_flag(20, 10, 'pink', 'pink')

# right wavy flag
moveto(200, 290)
tri_flag(20, 10, 'pink', 'pink')

# Little Boris the Tortoise heads for the flowers!
moveto(-50, -160)
turtle.color('black', 'wheat')

turtle.Screen().exitonclick()
