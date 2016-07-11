# Read first line
n, m = [int(x) for x in raw_input().split(" ")]

# Read in other lines
pyramid = [[0 for i in range(y+1)] for y in range(n)]

# Check if point is stable
def is_stable(p):
	global pyramid
	global n
	row = p[0]
	col = p[1]
	if (row == n - 1):
		return True

	if (pyramid[row + 1][col] and pyramid[row + 1][col+1]):
		return True

	else:
		return False

# stabilize a point recursively
def stabilize(point):
	global pyramid
	row = point[0]
	col = point[1]

	if (pyramid[row][col]) and (not is_stable(point)) and (row != n-1):
		pyramid[row + 1][col] = 1
		pyramid[row + 1][col + 1] = 1

		if not is_stable([row + 1, col]):
			stabilize([row + 1, col])

		if not is_stable([row + 1, col+1]):
			stabilize([row + 1, col+1])

coords = [[int(x) for x in raw_input().split(" ")] for i in range(m)]

for j,k in coords:
	pyramid[j-1][k-1] = 1


# stabilize every point
for w in range(len(pyramid)):
	for y in range(len(pyramid[w])):
		stabilize([w, y])

# Get the length of a list of all data in pyramid
total_data = len([x for x in sum(pyramid, []) if x])
print total_data