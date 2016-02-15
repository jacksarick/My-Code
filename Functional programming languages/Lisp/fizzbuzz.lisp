(print (loop for i from 0 to 20
	(cond 
		((= (mod i 3) 0) collect "Fizz")
		((= (mod i 5) 0) collect "Buzz")
		(t collect i))))