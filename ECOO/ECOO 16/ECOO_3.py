# big = max(cars)
# for x in cars[::-1]:
# 	if x == big:
# 		cars.pop()
# 	else
cars = [3,5,1,4,2]
big = max(cars)
print  zip(cars, [cars.index(x) for x in range(1,big)])
print {car: dist for car, dist in zip(cars, [cars.index(x) for x in range(1,big+1)])}