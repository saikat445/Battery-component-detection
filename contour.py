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
    imgColor, mask = myColorFinder.update(img_resize, hsvVals)
    #_,contours = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in mask:
        area = cv2.contourArea(cnt)
        print(area)

    #def get_contour_areas(contours):
        #all_areas = []
        #for cnt in contours:
            #area = cv2.contourArea(cnt)
            #all_areas.append(area)
        #return all_areas

    #sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
    #largest_item = sorted_contours[0]
    #cv2.drawContours(img_resize, largest_item, -1, (255, 0, 0), 10)

    cv2.imshow("img",img_resize)
    cv2.imshow("mask",mask)
    cv2.imshow('Largest Object', img_resize)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()