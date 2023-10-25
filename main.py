from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

scoreboard = Scoreboard()
player_name = screen.textinput(title="Snake Game", prompt="Name your snake:")

start_message = Turtle()
start_message.hideturtle()
start_message.color("white")
start_message.penup()
start_message.goto(0, 0)
start_message.write("PRESS SPACE TO START", align="center", font=("Arial", 30, "bold"))

snake = Snake()
food = Food()

pre_game = True


def start_game():
    global pre_game
    pre_game = False


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.righ)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="space", fun=start_game)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if pre_game:
        pass
    else:
        snake.move()

    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall:
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
        # scoreboard.game_over()

    # Detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # scoreboard.game_over()
            # game_is_on = False


screen.exitonclick()


# TODO:
# 1 Before game starts, ask player to input snake name
# 2 Ask player to start the game
# 3 Add timer T-5 sec till snake starts moving
# 4 When snake collides with walls or tail, reset game, and ask player if they want to try again
# 5 If player decides not to try again, clear screen, center display high-score for top 5 snakes
# 6 Add music (maybe)
# 7 Change snake color
