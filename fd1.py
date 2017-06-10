import cv2 as cv
import numpy as np

faceDetect = cv.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv.VideoCapture("http://192.168.43.1:8080/video");
while(True):
    ret, img = cam.read();
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    cv.imshow("Face", img);
    if(cv.waitKey(0)==ord('q')):
        cam.release()
        cv.destroyAllWindows()
        break
cam.release()
cv.destroyAllWindows()
