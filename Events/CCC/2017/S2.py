# Python 3
## But like it works fine in python3 if you change input -> raw_input
_ = int(input())
n = sorted(map(int, input().split(" ")))
m = len(n)//2
l, h = n[:m][::-1], n[m:]
#lol python y u make ^ me do dis
print(" ".join(map(str, sum(zip(l, h), ()))))