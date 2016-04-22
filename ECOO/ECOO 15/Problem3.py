from math import *
fileIn = open(raw_input("File: "))
rawData = [line.strip("\n") for line in fileIn]

basicData = rawData[0].split()
pinX = [0,0,0,0,0,0,0,0,0,0,0]
pinY = [0,0,0,0,0,0,0,0,0,0,0]
degreeOfAccuracy = int(basicData[6])+1
pinX[1] = float(basicData[0])*(10**int(basicData[1]))
pinY[1] = float(basicData[2])*(10**int(basicData[3]))
if pinX[1] >= 0:
	pinStringX = str(pinX[1])[:degreeOfAccuracy+2]
else:
	pinStringX = str(pinX[1])[:degreeOfAccuracy+3]
pinX[1] = float(pinStringX)
if pinY[1] >= 0:
	pinStringY = str(pinY[1])[:degreeOfAccuracy+2]
else:
	pinStringX = str(pinX[1])[:degreeOfAccuracy+3]
pinY[1] = float(pinStringY)
sideLength = float(basicData[4])
height = (sideLength*sqrt(3))/2
i = 2
while i < 11:
	if i == 2:
		pinX[i] = pinX[1] - sideLength/6
		pinY[i] = pinY[1] + height/3
	if i == 3:
		pinX[i] = pinX[1] + sideLength/6
		pinY[i] = pinY[1] + height/3
	if i == 4:
		pinX[i] = pinX[1] - sideLength/3
		pinY[i] = pinY[1] + (height/3)*2
	if i == 5:
		pinY[i] = pinY[1] + (height/3)*2
	if i == 6:
		pinX[i] = pinX[1] + sideLength/3
		pinY[i] = pinY[1] + (height/3)*2
	if i == 7:
		pinX[i] = pinX[1] - (sideLength/2)
		pinY[i] = pinY[1] + height
	if i == 8:
		pinX[i] = pinX[1] - (sideLength/6)
		pinY[i] = pinY[1] + height
	if i == 9:
		pinX[i] = pinX[1] + (sideLength/6)
		pinY[i] = pinY[1] + height
	if i == 10:
		pinX[i] = pinX[1] + (sideLength/2)
		pinY[i] = pinY[1] + height
	if pinX[i] > 0 and i != 7 and i != 10:
		pinStringX = str(pinX[i])[:degreeOfAccuracy+2]
		if int(str(pinX[i])[degreeOfAccuracy+3]) >= 5:
			pinX[i] = float(pinStringX)*(10**(int(degreeOfAccuracy)))
			pinX[i] = pinX[i] + 1
			pinX[i] = pinX[i]/(10**(int(degreeOfAccuracy)))
		else:
			pinX[i] = float(pinStringX)
	elif pinX[i] < 0 and i != 7 and i != 10:
		pinStringX = str(pinX[i])[:degreeOfAccuracy+3]
		if int(str(pinX[i])[degreeOfAccuracy+4]) >= 5:
			pinX[i] = float(pinStringX)*(10**(int(degreeOfAccuracy)))
			pinX[i] = pinX[i] - 1
			pinX[i] = pinX[i]/(10**(int(degreeOfAccuracy)))
		else:
			pinX[i] = float(pinStringX)
	if pinY[i] > 0:
		pinStringY = str(pinY[i])[:degreeOfAccuracy+2]
		if int(str(pinY[i])[degreeOfAccuracy+3]) >= 5:
			pinY[i] = float(pinStringY)*(10**(int(degreeOfAccuracy)))
			pinY[i] = pinY[i] + 1
			pinY[i] = pinY[i]/(10**(int(degreeOfAccuracy)))
		else:
			pinY[i] = float(pinStringX)
	elif pinY[i] < 0:
		pinStringX = str(pinY[i])[:degreeOfAccuracy+3]
		if int(str(pinY[i])[degreeOfAccuracy+4]) >= 5:
			pinY[i] = float(pinStringX)*(10**(int(degreeOfAccuracy)))
			pinY[i] = pinY[i] - 1
			pinY[i] = pinY[i]/(10**(int(degreeOfAccuracy)))
		else:
			pinX[i] = float(pinStringX)
	pinY[i] = float(pinStringY)
	i = i + 1
listedPins = []
i = 0
print len(rawData)
while i < len(rawData):
	print i
	if i > 1:
		compareX = float(rawData[i][0])*(10**int(rawData[i][1]))
		compareY = float(rawData[i][2])*(10**int(rawData[i][3]))
		j = 0
		while j < 11:
			if compareX == pinX[j] and compareY == pinY[j]:
				listedPins.append(j)
	i = i + 1
print listedPins