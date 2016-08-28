from random import randint
from math import floor
import matplotlib.pyplot as plt

SIZE  = 200
SEEDS = 20

arr = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
peaks = [(randint(0, SIZE-1), randint(0, SIZE-1), randint(3, 50)) for _ in range(SEEDS)]
# peaks = [(0,0,20), (0,199,20), (199,0,20), (199,199,20),]

for peak in peaks:
	for y in range(SIZE-1):
		for x in range(SIZE-1):
			dy = (peak[0] - y)
			dx = (peak[1] - x)

			dx = dx if dx > 0 else 1
			dist = floor(abs((dy/dx)/peak[2]))
			arr[y][x] += dist

# arr[1][1] = 9

# print arr
plt.imshow(arr)
plt.gray()
plt.show()