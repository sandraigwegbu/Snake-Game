from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.goto(x=0, y=260)
		self.color("white")
		self.hideturtle()
		self.score = 0
		with open("data.txt") as data:
			self.high_score = int(data.read())
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

	def reset_scoreboard(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open("data.txt", mode="w") as data:  # saves new high score to data.txt
				data.write(f"{self.high_score}")
		time.sleep(1)
		self.score = 0
		self.update_scoreboard()

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()
