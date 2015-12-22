from random import randint
rps = lambda c,u: ((c == u)*"Tie" + (c < u and u+2 == c)*"Win" + (not (c < u and u+2 == c))*"Loss")
print rps(randint(1,3), {"p":1, "s":2, "r":3}[raw_input("Your Move (p, s, r)\n>")])