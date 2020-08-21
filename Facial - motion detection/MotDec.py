# import everytging
import imutils
from imutils.video import VideoStream
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

#load in webcam (remember to remove sticker)
vs = VideoStream(src=0).start()

#initialize the first frame in the video stream
firstFrame = None

#loop through the frames of the video
while True:
	#get the current frame and initialize the text
	frame = vs.read()
	#text on frame
	text = "Unoccupied"
	#resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
	#get the absolute difference between the current frame and the first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	#dilate the thresholded image to fill in holes, then find contours on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	#loop over the contours
	for c in cnts:
		#if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue
		#draw boxes over moving parts and update text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"
		#Write the text
	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 105, 100), 2)
	#show the frame
	cv2.imshow("Motion detection", frame)
	#press esc to stop
	k = cv2.waitKey(30) & 0xff

	if k == 27:
		break
#stop the thing
cv2.destroyAllWindows()
