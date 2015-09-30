#hoffman
letter = ['A', 'B', 'C']
asocletter = ['00', '01', '10']
store, answer = [], []
bininput = list(raw_input(": "))

for i in range(len(bininput)):
	store.append(bininput[i])
		for n in range(len(asocletter)):
			if str(''.join(store)) == asocletter[n]:
				answer.append[letter(n)]
				store = []

print answer
