## CLOSE
### What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from math import factorial
print reduce(lambda x, y: x * y, filter(lambda n: factorial(n-1)%n == n-1, [i for i in range(1,21)]), 1)