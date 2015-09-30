fileinput = raw_input("File: ")
file = open(fileinput)
linelist = []
latin = []
english = []
positioninlist = 0
for line in file:
	linelist = line.split("<")
for i in range(len(linelist)):
	if "td class" in linelist:
		english.append('thing')
		positioninlist = positioninlist + 1
#	elif "span class='hw padded'" in linelist[positioninlist]:
#		latin.append(linelist[positioninlist])
#		positioninlist = positioninlist + 1
#	else:
#		postioninlist = positioninlist + 1
print(english)
