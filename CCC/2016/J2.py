# make
square = [[int(x) for x in raw_input().split(" ")] for i in range(4)]

# test case
# square = [[16,3,2,13], [5,10,11,8], [9,6,7,12], [4,15,14,1]]

# across
sums = [sum(square[i]) for i in range(4)] + [sum([square[x][y] for x in range(4)]) for y in range(4)]

# result
if sums.count(sums[0]) == len(sums):
	print "magic"

else:
	print "not magic"