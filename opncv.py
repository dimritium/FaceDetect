import numpy as np
#import Tkinter as tkinter
#import FileDialog
import cv2 as cv
from matplotlib import pyplot as plt

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
img = np.zeros((512,512,3), np.uint8)
img = cv.ellipse(img,(256,256),(100,50),10,10,180,360,0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
img = cv.line(img, (0,0), (511,511), (255,0,0),5)
img = cv.imread('Lenna.png',0)
cv.namedWindow('image',cv.WINDOW_NORMAL)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

img1 = cv.imread('Lenna.png',1)
cv.imshow('image',img)
k=cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imshow('image',img1)
cv.waitKey(0);

cv.waitKey(0)


#img2 = cv.imread('Lenna.png',-1)
#cv.imshow('imgage',img2)
#cv.waitKey(0);
#cv.imwrite('Lennagray.png',img)
#cv.destroyAllWindows()
#print img
