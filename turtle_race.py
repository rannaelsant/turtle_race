import turtle
from turtle import Turtle, Screen
import random as rd

is_race_on = False
random_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "orange", "purple", "pink"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    random_turtle = Turtle(shape="turtle")
    random_turtle.color(colors[turtle_index])
    random_turtle.penup()
    random_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(random_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = rd.randint(0, 1)
        turtle.forward(random_distance)


screen.exitonclick()