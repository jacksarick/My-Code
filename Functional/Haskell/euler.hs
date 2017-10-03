-- General purpose functions
(//) :: Integer -> Integer -> Integer
(//) x y = x `mod` y

multiples :: Integer -> [Integer]
multiples x = [y | y <- [2 .. x `div` 2], x//y == 0]

prime :: Integer -> Bool
prime x = multiples x == []

-- Problems
-- Problem 1: sum all numbers under 1000 div by 3 or 5
problem1 :: Integer
problem1 = sum [x | x <- [1..999], x//3==0 || x//5==0]

-- Problem 2: sum all even fib numbers under 4mil
fib :: [Integer]
fib = map fst $ iterate (\(x, y) -> (y, (x + y))) (0, 1)

problem2 :: Integer
problem2 = sum [x | x <- takeWhile (< 4000000) fib, even x]

-- Problem 3: largest prime factor of 600851475143
problem3 :: Integer
problem3 = [x | x <- multiples 600851475143, prime x] !! 0

-- ??? Problem 4: largest palindrome from product of 2 3-digit numbers
-- palindrome :: Integer -> Bool
-- palindrome x = show x == reverse (show x)

-- problem4 :: Integer
-- problem4 = takeWhile (\x -> not (palindrome x)) [x | x <- [999**2, 999**2..1],

-- Problem 5: smallest number evenly divisible by [1..20]
problem5 :: Integer
problem5 = until (\x -> foldl1 (&&) $ map (\y -> (x//y) == 0) [1..20]) (subtract 1) $ foldl1 (*) [1..20] - 1

-- Problem 6: ∆ sum of squares and square of sums
problem6 :: Integer
problem6 = (sum [1..100] * sum [1..100]) - (sum [x * x | x <- [1..100]]) 

-- Problem 7: 10001 prime number
problem7 :: Integer
problem7 = [x | x <- [1..], prime x] !! 10001


-- Main function
main :: IO ()
main = print $ problem1