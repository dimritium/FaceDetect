import cv2 as cv
img = cv.imread('Lenna.png')
lower_reso = cv.pyrDown(img)
cv.imshow("lr",lower_reso)
cv.waitKey(0)
cv.destroyAllWindows()