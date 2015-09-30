# Permute
from math import factorial as fct

#array = ['&', 'C', 'D', 'S', 'M']
array = ['A', 'B', 'C', 'D']
bigarray = []

def permute(listin, bigarray):
	for i in range(fct(len(listin))):
		listin.insert(2,listin[0])
		listin.pop(0)
		listin.insert(0,listin[-1])
		listin.pop(-1)


permute(array, bigarray)