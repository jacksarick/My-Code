import cv2
from time import time

starttime = time()

def readFrame(videoIn):
	# read video in
	video = cv2.VideoCapture(videoIn)
	# get amount of frames in video
	framecount = video.get(7)

	success = True
	counter = 0

	# loop through all frames
	while success:
		# read image, write out as a temp frame
		success, image = video.read()
		cv2.imwrite("./frame_img" + str(counter) + ".jpg", image)
		print "./frame_img" + str(counter) + ".jpg has been saved"
		counter += 1

readFrame(raw_input("Video to average: "))
print time() - starttime