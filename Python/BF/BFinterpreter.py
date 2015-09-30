#!/usr/bin/pythonw
'''A brainfuck interpreter written in python'''

BFinput = list(raw_input("Put BF here: "))
posBFinput = 0

otherinput = list(raw_input("Input: "))
posotherinput = 0

poscell = 0

for i in range(len(BFinput)):
	
	if BFinput[i] == ('+'):
		cell[poscell] += 1
	
	if BFinput[i] == ('-'):
		cell[poscell] -= 1
	
	if BFinput[i] == ('<'):
		poscell -= 1
	
	if BFinput[i] == ('>'):
		poscell += 1
	
	if BFinput[i] == (','):
		cell[poscell] = ord(otherinput[posotherinput])
		posotherinput += 1
	
	if BFinput[i] == ('.'):
		#print str(unichr(cell[poscell]))
		print cell[poscell]
	
	if BFinput[i] == ('['):
		if cell[poscell] != 0:
			tempposcell = poscell
			for j in range(len(BFinput)):
				if BFinput[tempposcell] == ']':
					poscell = tempposcell
					break
				else:
					tempposcell += 1
