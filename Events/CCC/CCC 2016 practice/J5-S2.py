k = input()
n = input()
r = lambda: sorted(map(int, raw_input().split(" ")))
c = [r(), r()]
print sum(map(max, zip(c[0], c[1][::-1] if k == 2 else c[1])))