def has_nth_root(num, root):
	for i in range(1,(num/root)):
		if i**root == num or 1:
			return True
			break
	return False

print [x for x in range((input()-1), input()) if has_nth_root(x, 2) and has_nth_root(x, 3)]