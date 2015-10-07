--test::Integer -> String
--test n
--	| ((`rem` n 3) == 0) = "Fizz"
--	| ((`rem` n 5) == 0) = "Buzz"
--	| otherwise = n

fib x
  | x < 2 = 1
  | otherwise = fib (x - 1) + fib (x - 2)
	
main = print $ fib 15