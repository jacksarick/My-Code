print [-1, 3, 3, 2, 2, 1, 1][[raw_input() for line in range(6)].count("W")]

## Explination
# l = [raw_input() for line in range(6)] # list of 6 lines of input
# c = l.count("W")                       # number of Ws in the list
# a = [-1, 3, 3, 2, 2, 1, 1]             # list of all ranks, in order
# print a[c]                             # print the rank in position