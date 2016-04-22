qtype, nil = input(), input()

di = 1 if qtype == 1 else -1

d = sorted([int(y) for y in raw_input().split(" ")])
p = sorted([int(y) for y in raw_input().split(" ")])

print sum([max(x) for x in zip(p,d[::di])])