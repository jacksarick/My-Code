fileIn = open(raw_input("File: "))
rawData = [line.strip("\r\n") for line in fileIn]
totalTime = 0
timeArray = []
flag = 0
#print rawData

#orange(0), blue(1), green(2), yellow(3), pink(4), violet(5), brown(6), red(7)
smartieData = [0, 0, 0, 0, 0, 0, 0, 0]
for i in rawData:
	if i == "orange":
		smartieData[0] += 1

	if i == "blue":
		smartieData[1] += 1

	if i == "green":
		smartieData[2] += 1

	if i == "yellow":
		smartieData[3] += 1

	if i == "pink":
		smartieData[4] += 1

	if i == "violet":
		smartieData[5] += 1

	if i == "brown":
		smartieData[6] += 1

	if i == "red":
		smartieData[7] += 1

	if i == "end of box":
		for i in range(0,7):
			while smartieData[i] > 0:
				smartieData[i] -= 7
				totalTime += 13

		totalTime += (smartieData[7]*16)
		timeArray.append(totalTime)
		totalTime = 0
		smartieData = [0, 0, 0, 0, 0, 0, 0, 0]



for element in timeArray:
	print str(element)