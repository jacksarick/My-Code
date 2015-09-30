

table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def winning():
	# 0=none 1=X 2=O
	for i in range(3):
		# | win
		if (table[0][i] == table[1][i] == table[2][i]):
			if table[0][i] == "X":
				return "X"
			elif table[0][i] == "O":
				return "O"
		# - win
		elif (table[i][0] == table[i][1] == table[i][2]):
			if table[i][0] == "X":
				return "X"
			elif table[i][0] == "O":
				return "O"
		# / or \ win
		elif (table[0][0] == table[1][1] == table[2][2]) or (table[0][2] == table[1][1] == table[2][0]):
			if table[0][0] == "X":
				return "X"
			elif table[0][0] == "O":
				return "O"
		else:
			return "N"

def display():
	print table[0][0] + " | " + table[0][1] + " | " + table[0][2]
	print "- + - + -"
	print table[1][0] + " | " + table[1][1] + " | " + table[1][2]
	print "- + - + -"
	print table[2][0] + " | " + table[2][1] + " | " + table[2][2]

while True:
	table[input("x coord: ")-1][input("y coord: ")-1] = "X"
	display()
