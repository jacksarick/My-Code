module Main where

-- sort :: Integer -> String
sort x
    | x mod 15 == 0 = "fizzbuzz"
    | x mod  5 == 0 = "buzz"
    | x mod  3 == 0 = "fizz"
    | otherwise   = show x :: String

main = print $ map sqrt [1..20]