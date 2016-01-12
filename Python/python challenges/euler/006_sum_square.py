## DONE
### Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
print (sum([n for n in range(101)])**2 - sum([n**2 for n in range(101)]))