from random import randint as rdnt

startmap = []
bombmap  = []

def genMap():
	startmap.append(["0 ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
	for i in range(10):
		startmap.append([])
		if i == 9:
			startmap[i+1].append(str(i+1))
		else:
			startmap[i+1].append(str(i+1) + " ")
		for j in range(10):
			startmap[i+1].append("#")


def displayMap():
	print "Flags Left: " + str(10 - flags)
	for i in range(11):
		print " ".join(startmap[i])

def genBombs():
	bombmap = [[rdnt(1,10), rdnt(1,10)] for i in range(7)]

def remap(x, y):
	bombs = 0
	relativeMap = [[y+1, x], [y+1, x+1], [y-1, x-1], [y-1, x], 
	[x+1, y], [x+1, y+1], [x-1, y-1], [x-1, y]]

	for 

	return bombs

genMap()
genBombs()
displayMap()