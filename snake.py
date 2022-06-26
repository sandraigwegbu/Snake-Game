from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Starting positions of each of the snake's three starting segments
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

	def __init__(self):
		self.snake_segments = []
		self.create_snake()
		self.head = self.snake_segments[0]

	def create_snake(self):
		# Create a snake body comprised of three square segments
		for position in STARTING_POSITIONS:
			self.add_segment(position)

	def add_segment(self, position):
		new_segment = Turtle("square")
		new_segment.color("white")
		new_segment.penup()
		new_segment.goto(position)
		self.snake_segments.append(new_segment)

	def reset(self):
		for seg in self.snake_segments:
			seg.goto(1000, 1000)
		self.snake_segments.clear()
		self.create_snake()
		self.head = self.snake_segments[0]

	def extend(self):
		# Adds a new segment to the snake
		self.add_segment(self.snake_segments[-1].position())  # adds a segment to position of last segment in list

	def move(self):
		# Make the tail follow the path of the head
		for seg_num in range(len(self.snake_segments) - 1, 0, -1):  # start (last segment), stop (first segment), step
			new_x = self.snake_segments[seg_num - 1].xcor()
			new_y = self.snake_segments[seg_num - 1].ycor()
			self.snake_segments[seg_num].goto(new_x, new_y)  # last segment moves to coord of 2nd last segment, and so on...

		self.head.forward(MOVE_DISTANCE)  # the snake is always moving while the game is on

	def up(self):
		# Make the snake travel in the 'up' direction
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		# Make the snake travel in the 'down' direction
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		# Make the snake travel in the 'left' direction
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		# Make the snake travel in the 'right' direction
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)
