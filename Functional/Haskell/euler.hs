-- General purpose functions
(//) :: Integer -> Integer -> Integer
(//) x y = x `mod` y

-- Problems
-- Problem 1
problem1 :: Integer
problem1 = sum [x | x <- [1..999], x//3==0 || x//5==0]

-- Problem 2
fib :: [Integer]
fib = map fst $ iterate (\(x, y) -> (y, (x + y))) (0, 1)

problem2 :: Integer
problem2 = sum [x | x <- takeWhile (< 4000000) fib, even x]

main :: IO ()
main = print $ problem1