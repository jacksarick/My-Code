# Python 2
from itertools import permutations
from collections import Counter

# _ = raw_input()
planks = map(int, raw_input().split(" "))

#[g][o][ ][f][u][c][k][ ][u][r][s][e][f][ ][g][u][i][d][o]

anser_stage_1 = [sum(x) for x in list(permutations(planks, 2))]

count = Counter()
for thing in anser_stage_1:
	count[thing] += 1
print count.most_common(1)[0][1]/2
