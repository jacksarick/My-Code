#letters = [' ', 'n', 'i', 't', 'e', 'y', 'b', 'o', 'l', 's', 'f', 'r', 'h', 'w', 'a', 't', 'k', 'd', 'p', 'r', 'u']
letters = []
array = list(raw_input(": "))
finalbfcode = []
#x bottles of beer on the wall x bottles of beer on the wall take one down pass it around x bottles of beer on the wall

# generates a simple 110 number in slot x
def genSimple(swoop):
	simple = []
	
	for z in range(10):
		simple.append('+')
	simple.append('[')
	
	for z in range(swoop):
		simple.append(">")

	for z in range(11):
		simple.append("+")

	for z in range(swoop):
		simple.append("<")
	simple.append('[')

	return simple

# customizes genSimple to a letter
def genBF(letterin, swoop):
	letter = ord(letterin)
	bfcode = genSimple(swoop)
	if letter > 110:
		for i in range(letter - 110):
			bfcode.append('+')
	elif letter < 110:
		for i in range(110 - (110 - letter)):
			bfcode.append('-')
	bfcode.append('.')
	return bfcode


for l in range(len(array)):
	if array[l] not in letters:
		letters.append(array[l])

print letters
for i in range(len(array)):
	finalbfcode.append(genBF(array[i], (i-1)))

for y in range(len(finalbfcode)):
	print finalbfcode[y],