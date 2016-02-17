# is palan -> li == li[::-1]

word = raw_input()

li = sum([[word[x:y] for y in range(x, len(word))] for x in range(len(word))], [])

print max([len(x) for x in li if x == x[::-1]])