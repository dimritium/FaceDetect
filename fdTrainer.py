import os
import cv2 as cv
import numpy as np
from PIL import Image

recogniser = cv.createLBPHFaceRecognizer();
detector = cv.CascadeClassifier("haarcascade_frontalface_default.xml");
path = 'dataSet'

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) ]
    faceSamples = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint 8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.dectectMultiScale(imageNp)
        for(x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y+h, x:x+w])
            Ids.append(Id)
