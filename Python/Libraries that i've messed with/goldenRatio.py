from turtle import *

def drawratio(start, rounds):
	radius = start
	for i in range(rounds):
		circle(radius, 90)
		radius **= 2

drawratio(10, 10)