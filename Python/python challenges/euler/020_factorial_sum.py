## DONE, but many is it dirty
### Find the sum of the digits in the number 100!
print sum(map(int, list(str(reduce(lambda x,y: x*y, [i for i in range(1,101)])))))