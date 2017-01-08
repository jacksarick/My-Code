# brings in a file to help take punctuation
import string
# import webcolors
from turtle import *

#Get our list of colours
colour_list = open("/Users/jack.sarick/Desktop/Program/list_of_colours.txt")
#breaks the list into lines
colour_list = [line.strip("\n").lower() for line in colour_list]

#Ask the user for the book
book = open(raw_input("Book: "))

#break book into lines
book_lines = [line.strip("\n") for line in book]

#Make an empty list of colours, since we havent found any colours yet
book_colours = []
book_hex = []

#Do this for every line in the book
for line in book_lines:

	#strip line of punctuation
	for c in string.punctuation:
		book_lines = line.replace(c,"")

	#Break the book into words and make them lower case
	book_lines = [word.lower() for word in book_lines.split(" ")]

	#Loop through this for every word in the line
	for word in book_lines:

		#if this word is in our list of colours, keep it
		if word in colour_list:

			#add the colour to our list
			book_colours.append(word)

			# try:
			# 	book_hex.append(webcolors.name_to_hex(word))
			# except ValueError:
			# 	book_hex = book_hex



#Finally, print all the colours, then the amount of them
# print book_hex
print book_colours
print len(book_colours)

# DRAW ALL THE colours

speed(0)

for draw_colour in book_colours:
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