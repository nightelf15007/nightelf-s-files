
#import everything
import numpy as np
import cv2

#I stole this file from the internet and it's what used to identify the face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#I stole this file from the internet and it's what used to identify the eyes (glasses makes things a bit janky and it sometimes picks up a mouth as eyes)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#load in webcam (remember to remove sticker)
cap = cv2.VideoCapture(0)

while True:
    #reads image from webcam
    ret, img = cap.read()
    #grey-scale the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #x and y and width and height
    for (x,y,w,h) in faces:
        #draw rectangle on image (max 2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(105,0,100),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #detect eyes inside face block
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #x and y and width and height
        for (ex,ey,ew,eh) in eyes:
            #draw blocks around eyes (max 2)
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #Show image
    cv2.imshow('Facial detection',img)
    k = cv2.waitKey(30) & 0xff
    #press escape to stop
    if k == 27:
        break
#Stop the thing
cap.release() 
cv2.destroyAllWindows()