from turtle import *

colour_list = ['#000000', '#0000ff', '#ffffff', '#ffffff', '#ffffff', '#000000', '#ffffff', '#ff0000', '#ffc0cb', '#0000ff', '#000000', '#000000', '#ffffff', '#0000ff', '#808080', '#ff0000', '#d2691e', '#ffffff', '#008000', '#008000', '#ffffff', '#000000', '#ffffff', '#0000ff', '#d2691e', '#d2691e', '#d2691e', '#0000ff', '#808080', '#ff0000', '#ffc0cb', '#d2691e', '#ffffff', '#0000ff', '#ff0000', '#000000', '#ffffff', '#ffffff', '#000000', '#808080', '#ffff00', '#0000ff', '#0000ff', '#000000', '#000000', '#ff0000', '#000000', '#ffffff', '#0000ff', '#0000ff', '#0000ff', '#000000', '#000000', '#0000ff', '#ffff00', '#ffffff', '#ffff00', '#0000ff', '#ffd700', '#ff0000', '#c0c0c0', '#d2691e', '#d2691e', '#d2691e', '#008000', '#ffffff', '#ffffff', '#ffffff', '#ff00ff', '#ff0000', '#ffffff', '#a52a2a', '#ffffff', '#ffff00', '#a52a2a', '#000000', '#ffff00', '#ff7f50', '#ff7f50', '#000000', '#a52a2a', '#ffd700', '#ffffff', '#a52a2a', '#d2691e', '#d2691e', '#d2691e', '#d2691e', '#d2691e', '#d2691e', '#ffffff', '#ffffff', '#c0c0c0', '#000000', '#ffffff', '#ffffff', '#000000', '#a52a2a', '#000000', '#000000', '#ffffff', '#000000', '#000000', '#ffff00', '#0000ff', '#ff0000', '#ff0000', '#ffffff', '#000000', '#ffffff', '#ffc0cb', '#ffff00', '#000000', '#ffffff', '#ffffff', '#f0e68c', '#000000', '#808080', '#ffffff', '#000000', '#ffff00', '#ffffff', '#000000', '#ffffff', '#000000', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#808080', '#808080', '#ff0000', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#008000', '#000000', '#008000', '#a52a2a', '#ffc0cb', '#ffff00', '#000000', '#800080', '#ffffff', '#000000', '#ffffff', '#ffffff', '#000000', '#ffffff', '#ffff00', '#000000', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ff0000']

speed(0)

for draw_colour in colour_list:
	if pos()[0] >= 200:
		penup()
		setpos(0, (pos()[1]-10))
		pendown()

	fillcolor(draw_colour)
	pencolor(draw_colour)
	begin_fill()
	for i in range(4):
		forward(10)
		right(90)
	end_fill()
	forward(10)

mainloop()