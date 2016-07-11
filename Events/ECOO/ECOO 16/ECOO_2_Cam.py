s = 3
p = [26,5,11]
w = 407
tr = ["*","+"]
# for i in range(s):
# 	for x in range(s):
# 		for k in range(s):
# 			for n in tr:
# 				for m in tr:
# 					if eval(str(p[i]) + str(n) + str(p[x]) + str(m) + str(p[k])) == str(w):
# 						print "works!"

# if w in map(sum, sum([[[[[(str(a),b,str(c),d,str(e)) for a in p] for b in tr] for c in p] for d in tr] for e in p], [])):
	# print "works"
arr = [[[[[("(", str(a),b,str(c), ")",d,str(e)) for a in p] for b in tr] for c in p] for d in tr] for e in p]
while True:
	try:
		arr = sum(arr, [])
		# print arr
	except Exception, e:
		break
# print ["".join(x) for x in map(list, arr)]
# print (["".join(x) for x in map(list, arr)])

print w in map(eval, ["".join(x) for x in map(list, arr)])
	# print "works"