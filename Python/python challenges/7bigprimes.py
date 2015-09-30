#DONE 5 lines, could be smaller
primes, a = [], 0
while len(primes) <= 10001:
	a += 1
	primes.append(a) if (all(a % i for i in xrange(2, a))) else "No"
print primes[-1]