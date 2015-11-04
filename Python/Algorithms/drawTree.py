from turtle import *
from json import loads

data = loads(raw_input("Data\n>"))

coords = {}

speed(0)

def drawNode(data):
	global coords
	nodes = len(data)
	degrees = 360/nodes
	nodenames = [key for key in data]

	for node in nodenames:
		penup()
		forward(100)
		dot(40, "grey")
		write(node, font=(30))
		coords[node] = pos()
		backward(100)
		left(degrees)

def mapNode(name):
	global coords
	global data

	for node in data[name]:
		penup()
		goto(coords[name][0], coords[name][1])
		pendown()
		goto(coords[node][0], coords[node][1])
		penup()

drawNode(data)

for node in data:
	mapNode(node)

mainloop()