date = input("")
while True:
	date += 1
	if len([x for x in list(str(date)) if list(str(date)).count(x) > 1]) == 0:
		print date
		break