#by Nikki Kim

# import turtle
from turtlesetup import *

# turtle draws example of a square.
turtle.goto(0, 0)
turtle.left(180)
turtle.forward(200)
turtle.down()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.up()

# turtle draws example of a triangle.
turtle.right(180)
turtle.forward(150)
turtle.down()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.up()

# turtle draws example of a pentagon.
turtle.left(120)
turtle.forward(150)
turtle.down()
turtle.forward(60)
turtle.left(72)
turtle.forward(60)
turtle.left(72)
turtle.forward(60)
turtle.left(72)
turtle.forward(60)
turtle.left(72)
turtle.forward(60)
turtle.up()
turtle.left(72)
turtle.forward(110)
turtle.up()

# turtle draws example of a star.
turtle.goto(230, 0)
turtle.down()
turtle.left(36)
turtle.forward(37)
turtle.right(72)
turtle.forward(37)
turtle.left(144)
turtle.forward(37)
turtle.right(72)
turtle.forward(37)
turtle.left(144)
turtle.forward(37)
turtle.right(72)
turtle.forward(37)
turtle.left(144)
turtle.forward(37)
turtle.right(72)
turtle.forward(37)
turtle.left(144)
turtle.forward(37)
turtle.right(72)
turtle.forward(37)
turtle.up()
turtle.right(72)
turtle.goto(50, 200)

print("Here are a square, a triangle, a pentagon, and a star!")

# program quizzes child to draw their own shape.
child_response = input("What would you like to draw?")

# child inputs triangle.
if child_response == "Triangle":

    # turtle clears screen to give clean state to draw new shape.
    turtle.clearscreen()

    # child inputs 6 triangle coordinates which are converted from strings to integers for use in math formulas.
    print("Great, show me a triangle!")
    x_first_triangle = int(input("Enter x coordinate of the first point:"))
    y_first_triangle = int(input("Enter y coordinate of the first point:"))
    x_second_triangle = int(input("Enter x coordinate of the second point:"))
    y_second_triangle = int(input("Enter y coordinate of the second point:"))
    x_third_triangle = int(input("Enter x coordinate of the third point:"))
    y_third_triangle = int(input("Enter y coordinate of the third point:"))

    # turtle draws the shape by connecting child's input coordinates.
    turtle.up()
    turtle.goto(x_first_triangle, y_first_triangle)
    turtle.down()
    turtle.goto(x_second_triangle, y_second_triangle)
    turtle.goto(x_third_triangle, y_third_triangle)
    turtle.goto(x_first_triangle, y_first_triangle)

    # calculation of the 3 distances between the triangle coordinates using formula distance=√((x2 – x1)² + (y2 – y1)²).
    distance_points_12 = ((x_first_triangle - x_second_triangle) ** 2 + (
            y_first_triangle - y_second_triangle) ** 2) ** (1 / 2)
    distance_points_23 = ((x_second_triangle - x_third_triangle) ** 2 + (
            y_second_triangle - y_third_triangle) ** 2) ** (1 / 2)
    distance_points_13 = ((x_first_triangle - x_third_triangle) ** 2 + (y_first_triangle - y_third_triangle) ** 2) ** (
            1 / 2)

    # checking if child input coordinates create a triangle.
    # shape is a triangle only if created shape meets the triangle inequality theorem a<b+c and b<a+c and c<a+b.
    if distance_points_12 + distance_points_23 > distance_points_13 and distance_points_12 + distance_points_13 > \
            distance_points_23 and distance_points_13 + distance_points_23 > distance_points_12:
        print("You got it right!")
    else:
        print("Sorry, that is not a triangle.")

# child inputs square.
elif child_response == "Square":

    # turtle clears screen to give clean state to draw new shape.
    turtle.clearscreen()

    # child inputs 8 square coordinates which are converted from strings to integers for use in math formulas
    print("Great, show me a square!")
    x_first_square = int(input("Enter x coordinate of the first point:"))
    y_first_square = int(input("Enter y coordinate of the first point:"))
    x_second_square = int(input("Enter x coordinate of the second point:"))
    y_second_square = int(input("Enter y coordinate of the second point:"))
    x_third_square = int(input("Enter x coordinate of the third point:"))
    y_third_square = int(input("Enter y coordinate of the third point:"))
    x_fourth_square = int(input("Enter x coordinate of the fourth point:"))
    y_fourth_square = int(input("Enter y coordinate of the fourth point:"))

    # turtle draws the shape by connecting the child's input coordinates in order of input.
    turtle.up()
    turtle.goto(x_first_square, y_first_square)
    turtle.down()
    turtle.goto(x_second_square, y_second_square)
    turtle.goto(x_third_square, y_third_square)
    turtle.goto(x_fourth_square, y_fourth_square)
    turtle.goto(x_first_square, y_first_square)

    # calculation of the side distances between the 4 square coordinates using formula d=√((x2 – x1)² + (y2 – y1)²).
    side_distance_12 = ((x_first_square - x_second_square) ** 2 + (y_first_square - y_second_square) ** 2) ** (1 / 2)
    side_distance_23 = ((x_second_square - x_third_square) ** 2 + (y_second_square - y_third_square) ** 2) ** (1 / 2)
    side_distance_14 = ((x_first_square - x_fourth_square) ** 2 + (y_first_square - y_fourth_square) ** 2) ** (1 / 2)
    side_distance_34 = ((x_third_square - x_fourth_square) ** 2 + (y_third_square - y_fourth_square) ** 2) ** (1 / 2)

    # calculation of the diagonal distances between point 1&3, and point 2&4 using formula d=√((x2 – x1)² + (y2 – y1)²).
    diagonal_distance_13 = ((x_first_square - x_third_square) ** 2 + (y_first_square - y_third_square) ** 2) ** (1 / 2)
    diagonal_distance_24 = ((x_second_square - x_fourth_square) ** 2 + (y_second_square - y_fourth_square) ** 2) ** (
            1 / 2)

    # checking if child input coordinates created a square.
    # shape is square only if the created shape have equal side distances and equal diagonal distances.
    if side_distance_12 == side_distance_23 == side_distance_34 == side_distance_14 and \
            diagonal_distance_13 == diagonal_distance_24:
        print("You got it right!")
    else:
        print("Sorry, that is not a square.")

# child inputs anything other than triangle or square or finishes drawing and checking triangle or square
turtle.exitonclick()
