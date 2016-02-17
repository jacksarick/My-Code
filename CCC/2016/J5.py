qtype = input()
input()

d = sorted([int(y) for y in raw_input().split(" ")])
p = sorted([int(y) for y in raw_input().split(" ")])


if qtype == 1:
	print sum([max(x) for x in zip(p,d)])

else:
	print sum([max(x) for x in zip(p,d[::-1])])