w = raw_input()
print max(map(len, sum([[w[x:y] for x in range(len(w)+1) if ((w[x:y] == w[x:y][::-1]) and (w[x:y] != ''))] for y in range(len(w)+1)], [])))

## Explination:
# l = len(w)+1                          # length of word
# s = [w[x:y] for x in l] for y in l]   # every possible substring
# s = sum(s, [])                        # flatten list
# s = filter(lambda x: x != '', s)      # filter all empty strings
# s = filter(lambda x: x == x[::-1], s) # filter all non-palindromes
# s = map(len, s)                       # get length of all palindromes
# print max(s)                          # get maximum