# Hello world in a frame 
# DONE: 8 lines
words, space, longword = raw_input(': ').split(' '), [], 0
for i in range(len(words)):
	if longword <= len(words[i]):
		longword = len(words[i])
print('*' * (longword + 4))
for z in range(len(words)):
	print('* ' + words[z] + (' '*(longword - len(words[z]))) + ' *')
print('*' * (longword + 4))