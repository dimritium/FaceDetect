import cv2 as cv
import numpy as np
import sqlite3

faceDetect = cv.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv.VideoCapture("http://192.168.43.1:8080/video");

def insertOrUpdate(Id, Name, Age, Gender, criminal_records):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Person where ID = " + str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        cmd = "UPDATE Person SET Name = " + str(Name) + " WHERE ID = "+str(Id)
    else:
        cmd = "INSERT INTO Person VALUES("+str(Id)+","+str(Name)+","+str(Age)+","+str(Gender)+","+str(criminal_records)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()  

id = raw_input('enter user id ')
name = raw_input('Enter your name ')
age = raw_input('Enter your age ')
gender = raw_input('Enter Gender ')
criminal_records = raw_input('Enter criminal records ')
insertOrUpdate(id, name, age, gender, criminal_records)

sampN = 0
while(True):
    ret, img = cam.read();
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampN=sampN+1;
        cv.imwrite("dataSet/User."+str(id).strip()+"."+str(sampN)+".jpg", gray[y:y+h, x:x+w])
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
        cv.waitKey(100);
    cv.imshow("Face", img)
    cv.waitKey(1);
    if(sampN>10):
        break;
cam.release()
cv.destroyAllWindows()
