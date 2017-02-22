x, y = input(), input()
v = lambda x: int(x < 0)
print [1,2,4,3][v(x) + (v(y)*2)]