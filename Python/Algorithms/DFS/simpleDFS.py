# A very simple Depth First Search that finds whether or not a target is in a data set
def DFS(tree, target):

	# for every node in our data tree, do the following:
	for node in tree:
		# If the node is the target, return it
		if node == target:
			print node
		
		# If we can explore the node, explore it
		if type(node) is list:
			DFS(node, target)

# Look for a number in the following set
DFS([1, 2, 3, [4, 5, 6, [7, 8]], 9, [10, 11]], 10)