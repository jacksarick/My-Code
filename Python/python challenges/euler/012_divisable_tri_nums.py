## Close
### What is the value of the first triangle number to have over five hundred divisors?
print max([len(m) for m in map(lambda k: [n for n in range(1,(k+1)) if k%n == 0], [sum(range(n)) for n in range(1,1000)])])