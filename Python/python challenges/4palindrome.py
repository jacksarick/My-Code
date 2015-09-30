palin = 0
a = 100
b = 100

def isPalin(num):
	num = list(str(num))
	for i in range(len(num)/2):
		if num[i] != num[endoflist]:
			return False
			break
		else:
			return True

def findPalin(a, b):
	global palin
	for i in range(899):
		c = a * b
		print(str(a) + ' * ' + str(b) + ' = ' + str(c))
		if isPalin(c):
			palin = c
			print "FOUND"
		a += 1

for i in range(899):
	b += 1
	findPalin(a, b)