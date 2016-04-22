def is_fantastic(p):
	p1 = p[0]
	p2 = p[1]
	p3 = p[2]

	if ((p1[0] == p2[0] or p1[1] == p2[1]) + (p3[0] == p2[0] or p3[1] == p2[1]) + (p1[0] == p3[0] or p1[1] == p3[1])) == 2:
		return True
	else:
		return False

points = [[int(x) for x in raw_input().split(" ")] for i in range(input())]

permutations = [[[(x, y ,z) for x in points] for y in points] for z in points]

while True:
	try:
		permutations = sum(permutations, [])
	except Exception, e:
		break

# print permutations
tris = [sorted(x) for x in permutations if is_fantastic(x)]

bt_tris = sum([[(j, k) for j in tris] for k in tris], [])

while True:
	try:
		permutations = sum(bt_tris, [])
	except Exception, e:
		break

print len(bt_tris)

bt_tris = [True for p in bt_tris if p[0][1] == p[1][1] and p[0] != p[1]]

print len(bt_tris)