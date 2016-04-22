fileIn = open(raw_input("File: "))
rawData = [line.strip("\n") for line in fileIn]

charLimit = rawData[0]
newString = rawData[1].split(" ")
charInLine = 0
flag = 0
while len(newString) > 0:
	if ((len(newString[0]) == charLimit) or ((len(newString[0]) + 1) == charLimit)):
		print newString[0]
	if len(newString[0]) > charLimit:
		print newString[0][:charLimit]
		newString.append(i[charLimit:], newString[0] + 1)
	if len(newString[0]) < charLimit:
		lineToPrint = str(newString[0]) + " "
		#counter = newString.index(i)
		if len(newString) > 1:
			while len(lineToPrint) < charLimit and len(newString) > 1:
				if len(lineToPrint) + len(newString[1]) > int(charLimit):
					newString.pop(0)
					break
				else:
					lineToPrint += (newString[1] + " ")
					newString.pop(0)
		else:
			print lineToPrint
			break
	print lineToPrint
print "====="