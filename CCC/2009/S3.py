# Make blank network
network = {}

def mk_friend(x, y):
	global network

	# Make the people if they don't exist
	if x not in network:
		network[x] = []

	if y not in network:
		network[y] = []

	network[x].append(y)
	network[y].append(x)

def rm_friend(x, y):
	global network

	network[x].remove(y)
	network[y].remove(x)

def num_friends(x):
	global network
	print len(network[x])

def num_friends_2(x):
	global network

	f = network[x]
	f2 = sum([network[j] for j in f], [])

	diff = len([k for k in f2 if k not in f])

def separation(x, y):
	global network
	paths = find_all_paths(network, x, y)
	if paths == []:
		print "Not connected."
	
	else:
		print min([len(k) for k in paths])

def find_all_paths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if not graph.has_key(start):
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = find_all_paths(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
		return paths

# Get first command
u_in = raw_input()
cmd = u_in[0]

# Run program
while cmd != "q":
	cmd = u_in[0]

	params = u_in.split(" ")

	if cmd == "i":
		mk_friend(params[1], params[2])

	if cmd == "d":
		rm_friend(params[1], params[2])

	if cmd == "n":
		print num_friends(params[1])

	if cmd == "f":
		print num_friends_2(params[1])

	if cmd == "s":
		print separation(params[1], params[2])