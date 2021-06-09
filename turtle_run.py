import turtle
import random

min_speed = 7
max_speed = 15

half_width = 650
half_num_turtles = 4
lane_width = 80

turtles = []
speeds = []
rankings = []

half_height = lane_width * half_num_turtles
num_turtles = 2 * half_num_turtles
display_font = ("Arial", 20, "normal")

def setup_racetrack():
    pen = turtle.Turtle()
    pen.pencolor("white")
    pen.pensize(5)
    pen.ht()
    pen.penup()
    pen.goto(-half_width, -half_height)
    pen.left(90)
    pen.pendown()
    pen.forward(2 * half_height)
    pen.penup()
    pen.goto(-half_width - 17, half_height + 20)
    pen.pendown()
    pen.write("Start", font=display_font)
    pen.penup()
    pen.goto(half_width, half_height)
    pen.pendown()
    pen.back(2 * half_height)
    pen.penup()
    pen.goto(half_width - 25, half_height + 20)
    pen.pendown()
    pen.write("Finish", font=display_font)
    pen.penup()
    pen.pensize(1)
    pen.pencolor("yellow")
    pen.right(90)
    for i in range(-half_num_turtles, half_num_turtles + 1):
        pen.goto(-half_width + 2, i * lane_width)
        pen.pendown()
        pen.forward(2 * half_width - 2)
        pen.penup()
    for i in range(-half_num_turtles, half_num_turtles):
        pen.goto(-half_width - 50, i * lane_width + lane_width / 2)
        pen.pendown()
        pen.write(f"{i + half_num_turtles + 1}", font=display_font)
        pen.penup()


def create_turtle(ycoor):
    turtle1 = turtle.Turtle(shape="turtle", visible=False)
    turtle1.penup()
    turtle1.goto(-half_width, ycoor)
    turtle1.showturtle()
    turtle1.color(
        random.randrange(0, 255),
        random.randrange(0, 255),
        random.randrange(0, 255))
    turtle1.turtlesize(3, 3, 2)
    turtle1.pencolor(
        random.randrange(0, 255),
        random.randrange(0, 255),
        random.randrange(0, 255))
    turtle1.turtlesize(outline=3)
    return turtle1


def setup_turtles():
    for i in range(-half_num_turtles, half_num_turtles):
        t = create_turtle(i * lane_width + lane_width / 2)
        turtles.append(t)


def initialize_speeds():
    for i in range(2 * half_num_turtles):
        speeds.append(random.randrange(min_speed, max_speed))

      
def race_turtles():
    min_speed = min(speeds)
    k = 0
    while k <= (2 * half_width / min_speed) + 1:
        for i in range(num_turtles):
            t = turtles[i]
            if t.xcor() < half_width:
                t.forward(speeds[i])
            else:
                turtle_id = i + 1
                if turtle_id not in rankings:
                    rankings.append(turtle_id)
        k += 1


def print_rankings():
    ranking_pen = turtle.Turtle()
    ranking_pen.pencolor(0, 100, 200)
    ranking_pen.ht()
    ranking_pen.penup()
    ranking_pen.goto(-half_width - 50, -half_height - 50)
    ranking_pen.pendown()
    ranking_pen.write(f"Arrival order: {rankings}", font=display_font)
    ranking_pen.penup()
    
                
def main():
    turtle.setup(200 + 2 * half_width, 200 + 2 * half_height)
    turtle.Screen().colormode(255)
    turtle.Screen().bgcolor(101, 140, 90)

    old_val = turtle.tracer()
    turtle.tracer(0, 0)
    
    setup_racetrack()

    turtle.update()
    turtle.tracer(old_val)

    setup_turtles()
    initialize_speeds()
    race_turtles()
    print_rankings()


if __name__ == "__main__":
    main()
