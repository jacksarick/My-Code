# Python 2
## But sometimes also python 3?

s = input()
r = lambda: map(int, raw_input().split(" "))
a = r()
b = r()
#Jank ass ragamuffin POS
print max([day+1 for day in range(s) if sum(a[:day+1]) == sum(b[:day+1])] + [0])