f = lambda x: 1 if x < 2 else f(x - 1) + f(x - 2)
print [f(x) for x in range(0,10)]