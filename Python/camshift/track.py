# import the necessary packages
import numpy as np
import argparse
import cv2
from random import randint

# initialize the current frame of the video, along with the list of
# ROI points along with whether or not this is input mode
frame = None
roiPts = []
inputMode = False
ball = {"x": 750, "y": 350, "vx": 40, "vy": 40, "p": 0, "op": 0}

def point_in_poly(x,y,poly):
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

def selectROI(event, x, y, flags, param):
	# grab the reference to the current frame, list of ROI
	# points and whether or not it is ROI selection mode
	global frame, roiPts, inputMode, ball

	if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4:
		roiPts.append((x, y))
		cv2.circle(frame, (x, y), 4, (0, 255, 0), 2)
		cv2.imshow("frame", frame)

def main():
	# grab the reference to the current frame, list of ROI
	# points and whether or not it is ROI selection mode
	global frame, roiPts, inputMode

	# setup the mouse callback
	cv2.namedWindow("frame")
	cv2.setMouseCallback("frame", selectROI)

	camera = cv2.VideoCapture(0)

	# initialize the termination criteria for cam shift, indicating
	# a maximum of ten iterations or movement by a least one pixel
	# along with the bounding box of the ROI
	termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
	roiBox = None

	# keep looping over the frames
	while True:
		# grab the current frame
		(grabbed, frame) = camera.read()
		frame = cv2.flip(frame,1)

		# check to see if we have reached the end of the
		# video
		if not grabbed:
			break

		# if the see if the ROI has been computed
		if roiBox is not None:
			# convert the current frame to the HSV color space
			# and perform mean shift
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)

			# apply cam shift to the back projection, convert the
			# points to a bounding box, and then draw them
			(r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
			pts = np.int0(cv2.cv.BoxPoints(r))
			cv2.polylines(frame, [pts], True, (255, 255, 255), 2)
			cv2.fillPoly(frame, [pts], (255, 255, 255))
			# find top left and bottom right for drawing
			# (x,y) = (x2 + x1)/2, (y2+y1)/2
			# x = (x2 +x1)/2
			drawPts = np.array(pts)
			s2 = drawPts.sum(axis = 1)
			tl2 = drawPts[np.argmin(s2)]
			br2 = drawPts[np.argmax(s2)]
			x = (br2[0] + tl2[0])/2
			y = (br2[1] + tl2[1])/2
			cv2.circle(frame, (x, y), 4, (0, 0, 0), 2)

			#draw pongball
			#1300x700

			if (ball["x"] + ball["vx"]) > 1300:
				ball["vx"] *= -1
				ball["x"] += ball["vx"]

			if (((ball["y"] + ball["vy"]) > 700) or ((ball["y"] + ball["vy"]) < 0)):
				ball["vy"] *= -1
				ball["y"] += ball["vy"]

			if (ball["x"] + ball["vx"]) < 0:
				ball["p"] += 1
				ball["x"] = 750
				ball["y"] = 350

			if point_in_poly((ball["x"] + ball["vx"]), (ball["x"] + ball["vx"]), pts):
				ball["vx"] *= -1
				ball["x"] += ball["vx"]
				ball["op"] += 1

			else:
				ball["x"] += ball["vx"]
				ball["y"] += ball["vy"]

			cv2.circle(frame, (ball["x"], ball["y"]), 10, (255, 255, 255), 2)

			cv2.putText(frame, ("Bounces: " + str(ball["op"])), (1000, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, 255) 
			cv2.putText(frame, (" Losses: " + str(ball["p"])), (1000, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, 255)

		# show the frame and record if the user presses a key
		cv2.imshow("frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# handle if the 'i' key is pressed, then go into ROI
		# selection mode
		if key == ord("i"):
			roiPts = []
			# indicate that we are in input mode and clone the
			# frame
			inputMode = True
			orig = frame.copy()

			# keep looping until 4 reference ROI points have
			# been selected; press any key to exit ROI selction
			# mode once 4  points have been selected
			while len(roiPts) < 4:
				cv2.imshow("frame", frame)
				cv2.waitKey(0)

			# determine the top-left and bottom-right points
			roiPts = np.array(roiPts)
			s = roiPts.sum(axis = 1)
			tl = roiPts[np.argmin(s)]
			br = roiPts[np.argmax(s)]


			# grab the ROI for the bounding box and convert it
			# to the HSV color space
			roi = orig[tl[1]:br[1], tl[0]:br[0]]
			roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

			# compute a HSV histogram for the ROI and store the
			# bounding box
			roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180])
			roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
			roiBox = (tl[0], tl[1], br[0], br[1])

		# if the 'q' key is pressed, stop the loop
		elif key == ord("q"):
			break

	# cleanup the camera and close any open windows
	camera.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()