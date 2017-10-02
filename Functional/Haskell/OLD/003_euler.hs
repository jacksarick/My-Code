isPrime :: Int -> Bool
isPrime y = 0 == (length [x | x <- [2..(y `div` 2)], y `mod` x == 0])

main = print $ head [x | x <- takeWhile (isPrime) [(600851475143 `div` 2),((600851475143 `div` 2) - 1)..1]]
--main = print [(600851475143 `div` 2), ((600851475143 `div` 2) - 1)..1]