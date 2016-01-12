## NOPE
### There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
# print zip([i for i in range(1,1000)], [j for j in range(1,1000)], [k for k in range(1,1000)])
# print filter(lambda a,b,c: (a**2) + (b**2) == c**2, zip([i for i in range(1,1000)], [j for j in range(1,1000)], [k for k in range(1,1000)]))