import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import  ColorFinder

cap = cv2.VideoCapture('2.jpeg')
myColorFinder= ColorFinder(False)
hsvVals = {'hmin': 12, 'smin': 0, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}


while True:
    _, img = cap.read()
    img = cv2.imread('2.jpeg')
    # img= img[0:900, :]
    img_resize = cv2.resize(img, (640, 480))
    _, mask = myColorFinder.update(img_resize, hsvVals)

    _, contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    print(contours)
    print('Numbers of contours found=' + str(len(contours)))




    cv2.imshow("img",img_resize)
    cv2.imshow("mask",mask)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()