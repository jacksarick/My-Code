## Theoretically works, just too lazy to actually run
### Find the sum of all the primes below two million.
from math import factorial
print sum(filter(lambda n: factorial(n-1)%n == n-1, [i for i in range(2,2000000)]))