#!/usr/bin/python
from __future__ import division
import matplotlib.pyplot as plt
from pylab import savefig
from random import randint
from time import time

filelocation = "/Users/jack.sarick/Desktop/Program/Python/pi/"
filename = filelocation + "pianswer.txt"
temppoint = []
temparray = []
loopcounter = 0
k50, k10, k5 = 50000, 10000, 5000

def makepi():
	global filelocation
	global filename
	global temparray
	counter = 0

	#Starts timer for loop
	looptime = time()

	#Generates points
	for i in range(k10):
		temppoint = [randint(0, k10), randint(0, k10)]
		if ((((temppoint[0]-k5)**2) + ((temppoint[1]-k5)**2)) < k5**2):
			plt.plot(temppoint[0], temppoint[1], 'bo')
			counter += 1
		elif ((((temppoint[0]-k5)**2) + ((temppoint[1]-k5)**2)) == k5**2):
			temparray.append([temppoint[0], temppoint[1]])
		else:
			plt.plot(temppoint[0], temppoint[1], 'ro')

	for element in temparray:
		plt.plot(temparray[element][0], temparray[element][1], 'gt')

	#Draws and saves file
	plt.axis([0, k10, 0, k10])
	savefig(filelocation + 'piwithgreen.png', bbox_inches='tight')

	#writes estimation and loop time to file
	with open(filename,'ab') as f: 
		f.write(str((counter/k50)*4) + "," + str(time()-looptime) + "\n")
		f.close()

#Runs makepi()
makepi()