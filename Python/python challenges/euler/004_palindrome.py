##CLOSE
### Find the largest palindrome made from the product of two 3-digit numbers.
print filter(
	lambda k: str(k)[len(str(k))/2:] == reversed(str(k)[:len(str(k))/2]),
	[a*b for a,b in zip([x for x in range(0,1000)], reversed([y for y in range(0,1000)]))]
)