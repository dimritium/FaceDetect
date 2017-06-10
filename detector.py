import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture("http://192.168.43.1:8080/video");
rec = cv2.face.createLBPHFaceRecognizer()
rec.load("recognizer/trainningData.yml")
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX

def getProfile(id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "select * from person where id = "+str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        print "Profile set"
        profile = row
    conn.close()
    return profile

while(True):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        Id = rec.predict(gray[y:y+h, x:x+w])
        print "Id",Id
        profile = getProfile(Id)
        print profile
        if(profile!=None):
            print "hi"
            cv2.putText(img, str(profile[1]), (x,y+h),font, 2, (255,0,0), 2, cv2.LINE_AA)
            cv2.putText(img, str(profile[2]), (x,y+h+80),font, 2, (255,0,0), 2, cv2.LINE_AA)
            cv2.putText(img, str(profile[3]), (x,y+h+120),font, 2, (255,0,0), 2, cv2.LINE_AA)
            cv2.putText(img, str(profile[4]), (x,y+h+160),font, 2, (255,0,0), 2, cv2.LINE_AA)
            
    cv2.imshow("Face", img);
    if(cv2.waitKey(1)==ord('q')):
        cv2.destroyWindow("Video")
        break
cam.release()
cv2.destroyAllWindows()
