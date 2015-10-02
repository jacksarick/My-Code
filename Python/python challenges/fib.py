from time import time
starttime = time()
def fib(n):
	a, b, c = 0, 1, 0
	for i in range(n-1):
		c = a + b
		b = a
		a = c
	return c

print fib(1000)
print time() - starttime