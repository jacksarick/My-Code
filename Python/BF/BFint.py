#!/usr/bin/pythonw
# A simple BF interpreter in Python

# A bunch of variables
cellBlock = []
pointer = 0

# builds a 3k cell block
def buildCellBlock():
	global cellBlock
	for i in range(3000):
		cellBlock.append(0)

buildCellBlock()
print(cellBlock)