from turtle import *

def drawPoly(n, lent):
	for i in range(n+1):
		forward(lent)
		left(float( 180 - ((n - 2) * (180 / n)) ))

for j in range(3,14):
	drawPoly(j,50)
done()