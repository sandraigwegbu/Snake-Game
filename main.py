from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # tracer(0) turns animation / automatic screen updates off

# Let's play
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
	screen.update()  # updates screen, used when tracer is off
	time.sleep(0.1)  # suspends execution for a given number of seconds

	snake.move()

	# Detect collision with food and increase score
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.update_score()

	# Detect collision with the wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		game_is_on = False
		scoreboard.game_over()

	# Detect collision with the snake's own tail
	for segment in snake.snake_segments[1:]:
		if snake.head.distance(segment) < 10:
			game_is_on = False
			scoreboard.game_over()


screen.exitonclick()



