import cv2
video = cv2.VideoCapture("/Users/jack.sarick/Desktop/Media/rgOdA9h.mp4")

count = 0
success,image = video.read()
while success:
	success,image = video.read()
	cv2.imwrite("./frame%d.jpg" % count, image)
	count += 1