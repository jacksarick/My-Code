#Problem J4: Wait Time
inputarray = []
for i in range(input()):
	inputarray.append(raw_input().split(" "))

#Number, total, lastwait, response
friendarray = []
ctime = 0
for i in range(len(inputarray)):
	if inputarray[i][0].lower() == "c":
		ctime += inputarray[i][1]

	if inputarray[i][0].lower() == "r":
		friendlist = [friendarray[j][0] for j in range(len(friendarray))]
		if (inputarray[i][1] not in friendlist):
			friendarray.append([inputarray[i][0].lower(), 0, ])
		else:
			location = friendlist.index(inputarray[i][1])
			friendarray[location] = [inputarray[i][1], friendarray[location] + ]
