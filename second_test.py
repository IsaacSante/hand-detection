import cv2
import numpy as np
import math  
print(cv2.__version__)

cam_width=800
cam_height=600
cam_set = 'v4l2src device=/dev/video0 ! video/x-raw, width='+str(cam_width)+',height='+str(cam_height)+',framerate=24/1 ! videoconvert ! appsink'
#cam = cv2.VideoCapture('/dev/video0')
cam = cv2.VideoCapture(cam_set)

while True:
	#read video frame
	ret, frame = cam.read()
	frame = cv2.flip(frame, 1)
	#convert to grayscale 
	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#apply gausian blur 
	value = (35, 35)
	blurred = cv2.GaussianBlur(grey, value, 0)
	_, thresh1 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	
	cv2.imshow('webcam_frame', thresh1)
	cv2.moveWindow('webcam_frame',0,0)
	if cv2.waitKey(1)==ord('q'):
	   break
cam.release()
cv2.destroyAllWindows()
