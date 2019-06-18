from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
camera.hflip=True
camera.vflip=True
# allow the camera to warmup
time.sleep(0.1)
#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print flags


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	#cropped = image[0:100, 0:400]

    # Convert BGR to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


        #define range of white color in HSV
        
        sensitivity = 15;
        lower_green = np.array([60 - sensitivity, 100, 50])  
        upper_green = np.array([60 + sensitivity, 255, 255]) 

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_green, upper_green)

        #ouverture fermeture
        kernel = np.ones((10,10),np.uint8)
        dilatation = cv2.dilate(mask,kernel,iterations = 1)
        
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(image,image, mask= dilatation)
        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

        ret, thresh= cv2.threshold(gray,140, 255, cv2.THRESH_BINARY)
        contours,h = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            perimetre=cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)

            if len(approx)>=8 :
                areaMax = 0
                cv2.drawContours(image,[cnt],-1,(0,255,0),2)
                for i in range(len(contours)):
                    area = cv2.contourArea(contours[i])
                    if area > areaMax:
                        areaMax = area
                        print areaMax

        cv2.imshow("frame",image)
        cv2.imshow("mask",mask)
        cv2.imshow("segmentation",thresh)
        cv2.imshow("resultat", res)

        k = cv2.waitKey(5) & 0xFF

        rawCapture.truncate(0)
        
        if k == ord('q'):
            break





cv2.destroyAllWindows()

