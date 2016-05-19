import sys

board = []
settings = {}

for line in sys.stdin:
	# If there is no line...
	if len(line) == 0:
		# Skip
		pass

	# If the line contains data, split it
	line = line.split(" ")

	# If it's settings...
	if line[0] == "settings":
		# Store game data
		settings[line[1]] = line[2]

	# If it's update...
	if line[0] == "update":
		# Store game update
		if line[2] == "round":
			game_round = int(line[3])
		if line[2] == "field":
			board = map(lambda x: x.split(","), line[3].split(";"))

	# If it's action...
	if line[0] == "action":
		# Preform and action
		pass

	# If it's not any of the above...
	else:
		# It's probably an error
		pass