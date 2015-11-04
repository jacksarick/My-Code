from string import ascii_uppercase
from random import randint
from json import dumps

nodes = input("Nodes?\n>")
max_connections = input("\nMax Connections?\n>")

def random_node(exclude):
	global nodes
	test = ascii_uppercase[:nodes][randint(0,nodes-1)]
	while test == exclude:
		test = ascii_uppercase[:nodes][randint(0,nodes-1)]	
	return test

data = \
	{
		ascii_uppercase[x]:[
			random_node(ascii_uppercase[x]) for n in range(max_connections)
		]
		for x in range(nodes)
	}

data = {d:list(set(data[d])) for d in data}

# print data
print dumps(data)