from math import pi
rawfile, average, counter, timeing = open("/Users/jack.sarick/Desktop/Program/Python/pi/pianswer.txt").read().split("\n"), 0, 0, 0
for i in rawfile:
	if (list(str(i))[0] == "3"):
		average += float(i.split(",")[0])
		timeing += float(i.split(",")[1])
		counter += 1
print "Pi = " + str(average/counter)
print "Time = " + str(timeing/counter)
print "Within " + str(1 - ((average/counter)/pi)) + "% of pi."
