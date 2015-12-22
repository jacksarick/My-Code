# triangulate
from sympy import *
from math import sqrt

# We're gonna need some variables
ax, ay, bx, by, cx, cy, dx, dy, n = symbols("ax, ay, bx, by, cx, cy, dx, dy, n")

ay = bx = cy = 0
ax = by = 1
cx = -1

ranges = [10, 20, 30]

a = Eq((((1-dx)*(0-dx))**-2), ranges[0])
b = Eq((((0-dx)*(1-dx))**-2), ranges[1])
c = Eq((((-1-dx)*(0-dx))**-2), ranges[2])
# print solve(c, solve(a, b))
solve(a, b)