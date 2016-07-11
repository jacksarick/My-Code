maze = {}
counter = 1

for i in range(input()):
	u_i = raw_input()
	u_i = [int(x) for x in u_i.split(" ")][::-1]
	maze[counter] = u_i[1:]
	counter += 1

def run_maze(start, path=[]):
	global maze
	graph = maze
	for node in maze[start]:
		path.append(node)
