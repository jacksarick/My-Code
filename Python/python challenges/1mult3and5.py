# Multiples of 3 and 5
# DONE: 1 line!
# [x for x in range(1000) if (x%3==0) or (x%5==0)]
answer = []

for numbers in range(1000):
	if (numbers % 3 == 0) or (numbers % 5 == 0):
		answer.append(numbers)
		
print sum(answer)