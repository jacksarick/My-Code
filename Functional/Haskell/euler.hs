-- General purpose functions
(//) :: Integer -> Integer -> Integer
(//) x y = x `mod` y

multiples :: Integer -> [Integer]
multiples x = [y | y <- [x `div` 2, (x `div` 2) - 1 .. 2], x//y == 0]

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

main :: IO ()
main = print $ problem3