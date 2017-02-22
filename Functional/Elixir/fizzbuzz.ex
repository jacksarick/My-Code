# Solution 1
fizzbuzz = fn
	x when rem(x, 15) == 0 -> "fizzbuzz"
	x when rem(x, 3) == 0 -> "fizz"
	x when rem(x, 5) == 0 -> "buzz"
	x -> x
end
IO.inspect Enum.map 1..20, fizzbuzz

# Solution 2
