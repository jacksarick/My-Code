w, a = raw_input(), raw_input()
print ["N", "A"][sum([abs(w.count(x) - a.count(x)) for x in set(w)]) == a.count("*")]