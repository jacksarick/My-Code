import pyglet
from pyglet.gl import *
from pyglet.window import key


from multi import m
from operator import mul
import math

sin = lambda x: math.sin(math.radians(x))
cos = lambda x: math.cos(math.radians(x))
adjust = lambda x: (x[0]+(WIDTH/2), x[1]+(HEIGHT/2))
mul_t = lambda x,y: (x[0]*y[0], x[1]*y[1])


black = (0, 0, 0)
white = (255, 255, 255)

WIDTH = 800
HEIGHT = 600
TICKS_PER_SEC = 60
FRICTION = 0.98
SPEED = 5

window = pyglet.window.Window(WIDTH, HEIGHT)
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

world = []

def draw_poly(*arg):
	arg = list(arg)
	s1 = map(adjust, arg)
	arg.append(arg.pop(0))
	s2 = map(adjust, arg)
	for line in zip(s1, s2):
		glColor3f(*white)
		glBegin(GL_LINES)
		glVertex2f(*line[0])
		glVertex2f(*line[1])
		glEnd()

def rotate(a, *arg):
	arg = list(arg[0])
	if a == 0:
		return arg
	
	verts = []

	for x,y in arg:
		# x = sum([cos(a), -sin(a)] |m| (x,y))
		# y = sum([sin(a),  cos(a)] |m| (x,y))
		x = x*cos(a) - x*sin(a)
		y = y*sin(a) + y*cos(a)
		verts.append((x,y))

	return verts


class Asteroid(object):
	""" x coord fo center, y coord of center, angle, radius
	(radius is half of the width)"""
	def __init__(self, x, y, a, r):
		self.x = x
		self.y = y
		self.a = a
		self.r = r
		world.append(self)
	
	def get(self):
		return (self.x, self.y, self.a, self.r)

	def draw(self):
		draw_poly(*self.get_vertices())

	def turn(self, a):
		self.a += a

	def update(self):
		self.turn(1)

	def get_corners(self):
		x = self.x
		y = self.y
		r = self.r

		return [
			(x+r, y+r), (x-r, y+r),
			(x-r, y-r), (x+r, y-r)
		]

	def get_vertices(self):
		return rotate(self.a, self.get_corners())

class Player(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.a = 0
		self.vx = 0
		self.vy = 0
		world.append(self)

	def speedUp(self):
		self.vx += cos(self.a)*SPEED
		self.vy += sin(self.a)*SPEED

	def turn(self, rot):
		self.a += rot

	def get_shape(self):
		x = self.x
		y = self.y

		return [
			(x, y+20), (x+20, y-20), (x, y-10), (x-20, y-20)
		]

	def get_vertices(self):
		return rotate(self.a, self.get_shape())

	def draw(self):
		draw_poly(*self.get_vertices())

	def update(self):
		self.vx *= FRICTION
		self.vy *= FRICTION
		self.x += self.vx
		self.y += self.y
		

@window.event
def on_draw():
	glEnable(GL_LINE_SMOOTH)
	glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
	glClear(GL_COLOR_BUFFER_BIT)
	map(lambda x: x.draw(), world)

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.Q:
		quit()

def update(time):
	map(lambda x: x.update(), world)
	if keyboard[key.UP]:
		player.speedUp()

	if keyboard[key.LEFT]:
		player.turn(-1)

	if keyboard[key.RIGHT]:
		player.turn(1)


# Setup
glClearColor(0, 0, 0, 1)
pyglet.clock.schedule_interval(update, 1.0 / TICKS_PER_SEC)

# glLineWidth(20)

test = Asteroid(0, 0, 10, 100)
# player = Player()
# print rotate(45, (1,1), (1,-1), (-1,1), (-1,-1))

pyglet.app.run()