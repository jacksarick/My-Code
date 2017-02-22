# Python 2

# Line 1 - variables
n, m, q = map(int, raw_input().split(" "))

# Line 2 - stations
lines = map(int, raw_input().split(" "))

# Line 3 - people map
people = map(int, raw_input().split(" "))

# Lines Q
actions = [map(int, raw_input().split(" ")) for _ in range(q)]
for action in actions:
	if action[0] == 1:
		print sum(people[action[1]-1:action[2]])

	else:
		stations = [x for x in range(n) if lines[x] == action[1]]
		movers = [people[x] for x in stations]
		# If it's stupid and it works, it ain't stupid
		movers = iter([movers[-1]] + movers[:-1])
		# ...yet somehow it's still fucking retarded
		for station in stations:
			people[station] = movers.next()