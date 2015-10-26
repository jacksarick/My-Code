from getch import getch

while True:
	key = ord(getch())
	if key == 27: #ESC
		break

	elif key == 119: #W
		move(1)

	elif key == 97: #A
		turn(1)

	elif key == 115: #S
		move(-1)

	elif key == 100: #D
		turn(-1)