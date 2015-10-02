from PIL import Image
from cv2 import VideoCapture, imwrite
from time import time

starttime = time()

def analyzeImg():
	# open the image
	img = Image.open("./tempimage.jpg")

	# grab width and height
	width, height = img.size

	# make a list of all pixels in the image
	pixels = img.load()
	data = []
	for x in range(width):
		for y in range(height):
			cpixel = pixels[x, y]
			data.append(cpixel)

	# set base RGB values
	r = 0
	g = 0
	b = 0
	counter = 0

	# loop through all pixels
	# if alpha value is greater than 200/255, add it to the average
	# (note: could also use criteria like, if not a black pixel or not a white pixel...)
	for x in range(len(data)):
		r += data[x][0]
		g += data[x][1]
		b += data[x][2]
		counter += 1;

	# compute average RGB values
	rAvg = r/counter
	gAvg = g/counter
	bAvg = b/counter

	# give average colour
	return (rAvg, gAvg, bAvg)

def readFrame(videoIn):
	# read video in
	video = VideoCapture(videoIn)
	# get amount of frames in video
	framecount = video.get(7)

	success = True

	colours = []

	# loop through all frames
	while success:
		# read image, write out as a temp frame
		success, image = video.read()

		imwrite("./tempimage.jpg", image)

		# try to analyze it
		try:
			print analyzeImg()
			colours.append(analyzeImg())
		except IOError:
			print "done"

	return colours

colours = readFrame(raw_input("Video to average: "))
print colours
fileout = open("./colours.txt", "w")
fileout.write(str(colours))
fileout.write("\nTime: " + str(time() - starttime))
fileout.close()