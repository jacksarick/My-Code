# Finds all circular primes

from math import factorial as fact
amount = 0

def isPrime(n):
    for i in range(2 , int(n ** 0.5) + 1 ):
        if n % i ==0:
            return False
    return True

def isPass(n):
	global amount
	num = list(str(n))
	standard = False

	if (n%2 != 0) or (n%3 != 0) or (n%5 != 0):
		for i in range(fact(len(num))):
			if isPrime(int(''.join(num))):
				standard = True
				num.append(num[0])
				num.pop(0)
			else:
				standard = False
				break
	else:
		standard = False
	
	if standard != False:
		amount += 1

	return standard

for q in range(input(": ")):
	isPass(q)