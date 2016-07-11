with open(raw_input("File\n-> ")) as file:
	for i in range(10):
		weights = [float(n)/100.0 for n in map(int, next(file).split(" "))]
		passes = 0
		size = int(next(file))
		for x in range(size):
			student = zip(map(int, next(file).split(" ")), weights)
			student = sum([x*y for x,y in student])

			if student >= 50.0:
				passes += 1

		print passes