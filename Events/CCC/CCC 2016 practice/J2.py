s = [map(int, raw_input().split(" ")) for _ in range(4)]
r = lambda x: sum(x)
print ["not magic", "magic"][len(set(map(r, s) + map(r, zip(*s[::1])))) == 1]