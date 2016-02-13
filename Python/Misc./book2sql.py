filein = open(raw_input(": "))
temp_array = []

for line in filein:
	temp_array = line.strip("\n").split(" by ")
	#print temp_array
	
	if len(temp_array) == 2:
		print "INSERT INTO `books_like` VALUES (NULL, '" + temp_array[0] + "', '" +temp_array[1] + "', ' ');"
	else:
		print "INSERT INTO `books_like` VALUES (NULL, '" + temp_array[0] + "', '" +temp_array[1] + "', '" + temp_array[2] + "');"