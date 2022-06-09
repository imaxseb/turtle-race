import time
from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=850, height=350)
screen.bgcolor("#222222")
screen.title("Turtle Race!")
screen.tracer(0)
COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
TITLE_FONT = ("Calibri", 30, "bold")
LANE_FONT = ("Calibri", 15, "bold")
RESULT_FONT = ("Calibri", 10, "normal")
all_turtles = []


def write_title():
    title = Turtle()
    title.hideturtle()
    title.penup()
    title.color("white")
    title.goto(x=0, y=125)
    title.write("--  TURTLE RACE!  --", align="center", font=TITLE_FONT)


def lane_numbers():
    lane_number = Turtle()
    lane_number.hideturtle()
    lane_number.penup()
    lane_number.color("white")
    for i in range(1, 7):
        lane_number.goto(x=-375, y=-150 + i * 40)
        lane_number.write(i, align="center", font=LANE_FONT)


def create_start_area():
    start_area = Turtle()
    start_area.hideturtle()
    start_area.penup()
    start_area.width(2)
    start_area.pencolor("white")
    start_area.goto(x=-360, y=120)
    start_area.pendown()
    start_area.goto(x=-360, y=-120)
    start_area.penup()
    start_area.goto(x=-395, y=120)
    start_area.pendown()
    start_area.goto(x=-395, y=-120)


def create_lane(height: int):
    lane_line = Turtle()
    lane_line.hideturtle()
    lane_line.penup()
    lane_line.goto(x=-395, y=height)
    lane_line.width(2)
    lane_line.pencolor("white")
    lane_line.pendown()
    lane_line.goto(x=380, y=height)


def create_finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.shape('square')
    finish_line.shapesize(0.5, 0.5)
    finish_line.width(2)
    finish_line.penup()
    for height in range(-115, 125, 10):
        for width in range(375, 390, 10):
            if (height + width) / 10 % 2 == 1:
                finish_line.color('white')
            else:
                finish_line.color('black')
            finish_line.goto(x=width, y=height)
            finish_line.stamp()


def create_turtles():
    for index, colour in enumerate(COLOURS):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colour)
        new_turtle.penup()
        new_turtle.goto(x=-380, y=index * 40 - 100)
        all_turtles.append(new_turtle)


def show_results(positions_dict: dict):
    background = Turtle()
    background.hideturtle()
    background.penup()
    background.goto(x=-20, y=-142.5)
    background.shape("square")
    background.shapesize(1, 36)
    background.color("black")
    background.stamp()
    result = Turtle()
    result.hideturtle()
    result.penup()
    locations = [-360, -240, -120, 0, 120, 240, 360]
    for (key, value), loc in zip(positions_dict.items(), locations):
        result.goto(x=loc, y=-150)
        result.color(key)
        result.write(f"{value}: {key.title()}", align="left", font=RESULT_FONT)


def countdown():
    count_turtle = Turtle()
    count_turtle.hideturtle()
    count_turtle.color("white")
    commands = ["3", "2", "1", "GO!!"]
    for command in commands:
        count_turtle.write(command, align="center", font=TITLE_FONT)
        time.sleep(1)
        count_turtle.clear()


def main():
    write_title()
    lane_numbers()
    create_start_area()
    lanes = [-120, -80, -40, 0, 40, 80, 120]
    for lane in lanes:
        create_lane(lane)
    create_finish_line()
    screen.tracer(1)
    create_turtles()
    countdown()

    screen.tracer(0)
    is_race_on = True
    positions = {}

    while is_race_on:
        screen.update()
        turtles_finished = 0
        position = len(positions) + 1
        for turtle in all_turtles:
            rand_dist = randint(0, 1)
            turtle.forward(rand_dist)
            if turtle.xcor() > 365:
                if turtle.color()[1] not in positions:
                    positions[turtle.color()[1]] = position
                turtles_finished += 1
                if turtles_finished == 6:
                    is_race_on = False

    show_results(positions)

    screen.exitonclick()


if __name__ == '__main__':
    main()
