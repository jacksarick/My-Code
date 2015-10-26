from getch import getch
while True:
	key = ord(getch())
	if key == 27: #ESC
		break
	elif key == 13: #Enter
		print("MORE!")
	elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
		key = ord(getch())
		if key == 80: #Down arrow
			print("Up up and away!")
		elif key == 72: #Up arrow
			print("we're going down")
	else:
		print(ord(getch()))