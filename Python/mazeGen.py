from random import randint

def genOutline(n):
	outline = []
	#Generate basic structure
	for i in range(n):
		outlineTMP = ["2" for i in range(n+2)]
		outlineTMP = [int(j) for j in list('1'.join(outlineTMP))]
		outline.append(outlineTMP)
		
		outlineTMP = ["1" for i in range(n+2)]
		outlineTMP = [int(j) for j in list('0'.join(outlineTMP))]
		outline.append(outlineTMP)

	#finish bottom and top
	outline.append([2 for i in range(2*(n+1)+1)])
	outline[0] = [2 for i in range(2*(n+1)+1)]

	#define centre points
	for row in outline:
		row[0] = 2
		row[-1] = 2

	#entry and exit points
	outline[0][1] = 0
	outline[-1][-2] = 0

	#randomize gates
	outline = [
		[randint(0,1) if x==1 else x for x in row] 
		for row in outline
	]

	return outline

def fillMaze(inArray):
	#convert to human
	newMap = [["#" if x!=0 else " " for x in row] for row in inArray]
	return newMap

#execute
k = fillMaze(genOutline(input("Size: ")))


for row in k:
	print ' '.join(str(l) for l in row)