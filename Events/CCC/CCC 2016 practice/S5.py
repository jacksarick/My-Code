[_, t] = map(int, raw_input().split(" "))
g = map(int, list(raw_input()))
c = lambda x: [x[n-1] != x[(n+1) % len(x)] for n in range(len(x))]
r = lambda f, a, t: a if t == 0 else r(f, f(a), t-1)
print "".join([str(int(n)) for n in r(c, g, t)])