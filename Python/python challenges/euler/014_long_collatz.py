## Theoretically Done (recursion limit), unlikely to be done in one line
### Which starting number, under one million, produces the longest chain

def collatz(n, counter=0):
	counter += 1
	if n == 1:
		return (n, counter)
	else:
		return collatz(n/2 if n%2==0 else (3*n)+1, counter)

longest = (0, 0)
for i in range(0,1000000):
	if longest[0] < collatz(i):
		longest = (collatz(i), i)

print longest