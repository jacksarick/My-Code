def fib(x):
	if x < 2:
		return 1
	else:
		return (fib(x - 1) + fib(x - 2))

n, q, t = 0, 0, 0
while n > 4000000:
	n = fib(q)
	t += n if n%2 == 0 else 0
	q += 1
print n