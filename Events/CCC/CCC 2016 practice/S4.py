# input()
b = map(int, raw_input().split(" "))
for e in range(1, len(b)):
	if b[e] != b[e-1]:
		yield b[e-1]
	else:
