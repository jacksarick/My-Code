import pyglet
from pyglet.gl import *
from pyglet.window import key

import math
from math import sqrt
from random import randint

# World Constants
WIDTH = 800
HEIGHT = 600
# MAX_DISTANCE = 30

# Game variables
focal_length = 1.6
resolution = 100.0

# Useful shortcuts 
black = (0,0,0)
white = (255, 255, 255)
red   = (255, 0, 0)
sin   = lambda x: math.sin(math.radians(x))
cos   = lambda x: math.cos(math.radians(x))
atan2 = lambda x,y: math.atan2(math.radians(x), y)
floor = lambda x: int(math.floor(x))
ceil  = lambda x: int(math.ceil(x))

rand_color = lambda: (randint(0,255), randint(0,255), randint(0,255))

window = pyglet.window.Window(WIDTH, HEIGHT)

class World(object):
	def __init__(self, world):
		self.world = world
		self.w = len(world[0])
		self.h = len(world)

	def get(self):
		return self.world

	def at(self, x, y):
		return self.world[y][x]

	def set(self, x, y, h):
		self.world[y][x] = h

	def addSquare(self, X, Y, n, z):
		for y in xrange(Y,Y+n):
			for x in xrange(X,X+n):
				self.world[y][x] = z

	def castRay(self, px, py, angle):
		# We're in the right quadrant if the angle is less than 180
		right = (angle < 180) 

		aSin = sin(angle)
		aCos = cos(angle)

		# Distance to block hit
		dist = 0

		# The slope of the straight line made by the ray
		slope = aSin / aCos

		# We move either 1 map unit to the left or right
		dX = 1 if right else -1

		# How much to move up or down
		dY = dX * slope

		# Starting x and y
		x = ceil(px) if right else floor(px)
		y = py + ((x - px) * slope)

		while (x >= 0 and x < self.w and y >= 0 and y < self.h):
			wallX = floor(x + (right-1))
			wallY = floor(y)

			# Is this point inside a wall block?
			if (self.at(wallX, wallY) > 0):
				distX = x - player.x
				distY = y - player.y
				# The distance from the player to this point, squared
				dist = distX*distX + distY*distY

				# Figure out height of wall based on distance
				# height / (distance * cos(angle))
				return self.at(wallX, wallY) / (dist * aCos)
				break

			# If not, increase the search distance
			x += dX
			y += dY
		return False


class Point(object):
	def __init__(self, x, y, d, w):
		self.x = x
		self.y = y
		self.dir = d
		self.world = w

	def get(self):
		return (self.x, self.y, self.dir)

	def getPos(self):
		return (self.x, self.y)

	def getDir(self):
		return self.dir

	def move(self, x, y):
		self.x += x
		self.y += y

	def turn(self, d):
		self.dir += d
		if self.dir >= 360:
			self.dir = 0
		if self.dir < 0:
			self.dir += 360

	def getView(self):
		view_map = []
		angle = self.getDir()
		for i in range(int(resolution)):
			view_map.append(self.world.castRay(
				self.getPos()[0],
				self.getPos()[1],
				self.getDir() * atan2(i, focal_length)
			))
		return map(lambda x: x*HEIGHT, view_map)

		
@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)

	# Draw Background
	glBegin(GL_POINTS)
	for x in xrange(WIDTH):
			for y in xrange(HEIGHT):
					if y > HEIGHT*.5:
						glColor3f(*white)
					else:
						glColor3f(*black)
					glVertex2i(x, y)
	glEnd()

	# Setup for drawing player view
	glLineWidth(WIDTH/resolution)
	glColor3f(*red)
	glEnable(GL_LINE_SMOOTH);
	glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)

	# Draw player view
	x = 0.0
	for p in player.getView():
		if p:
			glBegin(GL_LINES)
			glVertex2f(x, p+(HEIGHT/2))
			glVertex2f(x, -p+(HEIGHT/2))
			glEnd()
		x += WIDTH/resolution

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.Q:
		quit()
	elif symbol == key.X:
		print player.get()
	elif symbol == key.W:
		player.move(1, 0)
	elif symbol == key.S:
		player.move(-1, 0)
	elif symbol == key.A:
		player.turn(-1)
	elif symbol == key.D:
		player.turn(1)

world = World([[0 for x in range(32)] for y in range(32)])
# world.set(3, 3, 1)
world.addSquare(3, 3, 5, 1)
player = Point(2, 2, 315, world)

pyglet.app.run()