#Python 2

n, m, d = map(int, raw_input().split(" "))

pipes = [map(int, raw_input().split(" ")) for _ in range(m)]
pipes, inactive = pipes[:-1], pipes[-1]

cost = lambda city: return sum([p[2] for p in pipes])

