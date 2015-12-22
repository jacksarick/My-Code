from math import factorial
print filter(lambda n: factorial(n-1)%n == n-1, [i for i in range(1,10000000)])