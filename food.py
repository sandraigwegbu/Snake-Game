from turtle import Turtle
import random


class Food(Turtle):  # inherit all the methods and attributes of the Turtle superclass
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_wid=0.5, stretch_len=0.5)
		self.color("orange")
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		random_x = random.randint(-270, 280)
		random_y = random.randint(-280, 270)
		self.goto(random_x, random_y)
