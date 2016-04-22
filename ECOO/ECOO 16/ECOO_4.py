from math import sqrt

#input
with open(raw_input("File\n-> ")[:-1]) as file:
	for i in range(10):
		housepos = []

		housepos.append(map(int, next(file).split(" ")))
		for i in range(19):
			house = next(file).split(" ")
			house[0] = int(house[0])
			house[1] = int(house[1])
	 		housepos.append(house)

		housedist = []

		houseX = [k[0] for k in housepos]
		houseY = [k[1] for k in housepos]
		houseP = [k[2][0] for k in housepos[1:]]

		def dist(x1, y1, x2, y2):
			#print sqrt((x1-x2)**2.0 + (y1-y2)**2.0)
			return sqrt((x1-x2)**2.0 + (y1-y2)**2.0)

		for n in range(len(housepos)-1):
			housedist.append([dist(houseX[0], houseY[0], houseX[n], houseY[n]), houseP[n]])

		housedist = sorted(housedist)
		#print housedist
		deciders = [housedist[0], housedist[1], housedist[2]]

		#If dist = housedist[2] for any others (disregard pol standing) add it
		for x in range(len(housedist) -1):
			if x != 2:
				if housedist[x] == housedist[2]:
					deciders.append(housedist[x])

		houseP = [k[1] for k in housedist]
		pol = []
		for standing in houseP:
			if standing == "D":
				pol.append(1)
			else:
				pol.append(0)

		total = sum(pol)
		# print "pol: " + str(pol)

		average = (float(total)/float(len(pol)) * 100.0)
		print str(average)[:3]