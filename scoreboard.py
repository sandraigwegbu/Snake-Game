from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.goto(x=0, y=260)
		self.color("white")
		self.hideturtle()
		self.score = 0
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
		self.score += 1

	def game_over(self):
		self.penup()
		self.goto(0, 0)
		self.write("GAME OVER", align=ALIGNMENT, font=FONT)
