from json import loads

data = loads(raw_input("Data\n>"))

# DOESNT WORK

def depthFirstSearch(tree, start, target, result=[]):
	# make path
	path = result + [start]

	for node in tree[start]:
		if target in node:
			return result

		if start in node:
			pass

		else:
			depthFirstSearch(tree[node], node, target, path)

# print data['A'][0]
print depthFirstSearch(data, "A", "E")