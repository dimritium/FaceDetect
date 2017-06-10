# for training the data set
import os

import numpy as np
from PIL import Image

import cv2 as cv

recognizer=cv.face.createLBPHFaceRecognizer()
path = 'dataSet'
def getImagesWithID(path):
    print os.listdir(path)
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        print imagePath
        faceImg = Image.open(imagePath).convert('L') #converting into greyscale
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print ID
        IDs.append(ID)
        cv.imshow('training', faceNp)
        cv.waitKey(10)
    return IDs, faces
Ids, faces = getImagesWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainningData.yml')
cv.destroyAllWindows()
