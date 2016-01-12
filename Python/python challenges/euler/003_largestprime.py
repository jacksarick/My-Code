## WTF is a prime factor?
### What is the largest prime factor of the number 600851475143 ?
from math import factorial, sqrt
print max([lambda n: factorial(p-1)%n == p-1, [n for n in range(int(sqrt(600851475143)), 600851475143)]])