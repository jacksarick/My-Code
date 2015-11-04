def DFS(tree, target):
	for node in tree:
		if node == target:
			print node
		
		if type(node) is list:
			DFS(node, target)

data = [1, 2, 3, [4, 5, 6, [7, 8]], 9, [10, 11]]

DFS(data, 22)