fibs = 1 : 2 : zipWith (+) fibs (tail fibs)

main = print $ sum [x | x <- takeWhile (<= 4000000) fibs, even x]