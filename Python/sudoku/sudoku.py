## Grecco-Latin square Sudoku solver
s1 = [5, 0, 9, 1, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 9, 0, 4, 0, 1, 0, 7, 0, 6, 0, 0, 0, 9, 0, 9, 0, 0, 7, 0, 6, 0, 0, 6, 0, 0, 2, 0, 5, 0, 0, 1, 0, 0, 1, 0, 3, 0, 0, 9, 0, 9, 0, 0, 0, 1, 0, 3, 0, 6, 0, 8, 0, 9, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 6, 0, 0, 2]
s2 = [9, 0, 0, 8, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 4, 0, 3, 0, 0, 0, 4, 0, 3, 0, 0, 0, 8, 6, 0, 0, 5, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0, 9, 0, 0, 4, 0, 0, 6, 0, 3, 0, 0, 2, 3, 0, 0, 0, 5, 0, 1, 0, 0, 0, 5, 0, 1, 0, 0, 0, 9, 0, 0, 0, 7, 0, 0, 9, 0, 0, 5]

sec = [(0, 3), (3, 6), (6, 9)] * 3
lns = [(1, 2, 3)]*3 + [(4, 5, 6)]*3 + [(7, 8, 9)]*3

nums   = range(1,10)

check  = lambda arr: False not in [(x in nums and arr.count(x) == 1) for x in arr]
contra = lambda arr: False not in [(arr.count(x) == 1) for x in arr if x != 0]
row    = lambda arr, x: arr[(9*(x-1)):(9*(x-1))+9]
column = lambda arr, x: [arr[k] for k in range(x-1,81,9)]
sector = lambda arr, x: sum([row(arr, k)[sec[x-1][0]:sec[x-1][1]] for k in lns[x-1]], [])
check_all = lambda arr: False not in sum([[contra(row(arr, x)), contra(column(arr, x)), contra(sector(arr, x)),] for x in nums], [])
solved = lambda arr: False not in sum([[check(row(arr, x)), check(column(arr, x)), check(sector(arr, x)),] for x in nums], [])
def diff(a1,a2):
	d = []
	for x in range(len(a1)):
		if a1[x] not in a2:
			d.append(str(a1[x] + "=>" + str(a2[x])))
		else:
			d.append("")

def options(arr, ro, co):
	dup = list(arr)
	works = []
	for num in nums:
		dup[(((ro-1)*9)+co-1)] = num
		if check_all(dup):
			works.append(num)

	return works

def solver(arr):
	org = list(arr)
	counter = 0
	while 0 in arr and counter < arr.count(0):
		for ro in nums:
			for co in nums:
				if arr[(((ro-1)*9)+co-1)] == 0:
					guess = options(arr, ro, co)
					print ro, co, guess


					if len(guess) == 1:
						arr[(((ro-1)*9)+co-1)] = guess[0]
		counter += 1
	if arr == org:
		return False
	return arr

print solver(s1)