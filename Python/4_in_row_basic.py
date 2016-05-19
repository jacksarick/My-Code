import sys

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
		pass

	# If it's update...
	if line[0] == "update":
		# Store game update
		pass

	# If it's action...
	if line[0] == "action":
		# Preform and action
		pass

	# If it's not any of the above...
	else:
		# It's probably an error
		pass