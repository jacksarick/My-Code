def quicksort(arr):
	# print "Sorting " + ",".join(map(str, arr))
	p = arr[-1]
	for i in range(len(arr)-1):
		print arr[i]
		if arr[i] > p:
			arr.append(arr.pop(i))

	if len(arr) < 2:
		return arr

	else:
		p = arr.index(p)
		return quicksort(arr[p:]) + quicksort(arr[:p])

print quicksort([3, 7, 8, 6, 2, 1, 9, 5, 4])