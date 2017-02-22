s = map(int, raw_input().split(" "))
e = map(int, raw_input().split(" "))
c = input()
d = abs(s[0] - e[0]) + abs(s[1] - e[1])
print ["N", "Y"][(d <= c) and (((c - d) % 2) == 0)]