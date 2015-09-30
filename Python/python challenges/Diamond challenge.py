# Diamond challenge 
# DONE: 8
# Could be smaller
num = input(': ')
i = 1
while i < num:
	print( ((((num-1)/2)-(i/2)) *' ')+(i*'*'))
	i += 2
while i >= 0:
	print( ((((num-1)/2)-(i/2)) *' ')+(i*'*'))
	i -= 2