with open(raw_input("File\n-> ")) as file:
	for q in range(3):
		s = next(file)
		p = map(int, next(file).split(" "))
		w = map(int, next(file).split(" "))
		tr = ["*","+"]

		arr = [[[[[("(",str(a),b,str(c), ")",d,str(e)) for a in p] for b in tr] for c in p] for d in tr] for e in p]
		while True:
			try:
				arr = sum(arr, [])
			except Exception, e:
				break
		
		for val in w:
			if (val in map(eval, ["".join(x) for x in map(list, arr)])):
				print "T",
			else:
				print "F",
		print "\n"
