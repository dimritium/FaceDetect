import cv2 as cv
import numpy as np

img1 = cv.imread("Lenna.png");
img2 = cv.imread("mi.png");

dst = cv.addWeighted(img1,0.7,img2,0.3,1);
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
