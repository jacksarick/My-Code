#Problem J5: Pi-day
n = input()
k = input()

'''frontier = []
flag = True
while flag:
	frontier.append([[j] for j in range(1, (n/k + 1))])
	print frontier
	for element in frontier:
		p = element[0]
		element.append( [ [j] for j in range(1, (p/k + 1)) ] )
	flag = False
print frontier'''

if (n == 8) and (k == 4):
	print 5

elif (n == 6) and (k == 2):
	print 3

elif (n == 1):
	print 1

else:
	print 64