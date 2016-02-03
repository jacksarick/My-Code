def sumac(int_1, int_2, path=2):
	if (int_1 - int_2) >= 0:
		path += 1
		sumac(int_2, (int_1 - int_2), path)
	
	else:
		print path

sumac(120, 71)