from PIL import Image

def analyze():
	# open the image
	img = Image.open("/Users/jack.sarick/Desktop/Media/mario.jpg")

	# grab width and height
	width, height = img.size

	# make a list of all pixels in the image
	pixels = img.load()
	data = []
	for x in range(width):
		for y in range(height):
			cpixel = pixels[x, y]
			data.append(cpixel)

	r = 0
	g = 0
	b = 0
	counter = 0

	# loop through all pixels
	# if alpha value is greater than 200/255, add it to the average
	# (note: could also use criteria like, if not a black pixel or not a white pixel...)
	for x in range(len(data)):
		# if data[x][3] > 200:
		r += data[x][0]
		g += data[x][1]
		b += data[x][2]
		counter += 1;

	# compute average RGB values
	rAvg = r/counter
	gAvg = g/counter
	bAvg = b/counter

	return (rAvg, gAvg, bAvg)

print(analyze())