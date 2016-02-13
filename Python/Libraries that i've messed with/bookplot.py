#Plots the use of a word in a file
# X is sentence, Y is position

import matplotlib.pyplot as plt

filein = open(raw_input("First File: "), 'r')
word = raw_input("Word: ")

pointarray = []

splitfile = filein.read().split(".")

for j in range(len(splitfile)):
	myline = splitfile[j].split(" ")
	for i in range(len(myline)):
		if myline[i].upper() == word.upper():
			pointarray.append([j, i])

for n in range(len(pointarray)):
	plt.plot(pointarray[n][0], pointarray[n][1], 'bs')

plt.title("Usage of the word " + word)
plt.xlabel('Sentence')
plt.ylabel('Position')
plt.show()