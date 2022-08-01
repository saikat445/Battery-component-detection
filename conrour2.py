import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import  ColorFinder

cap = cv2.VideoCapture('2.jpeg')

while True:
    _, img = cap.read()
    img = cv2.imread('2.jpeg')
    img_resize = cv2.resize(img, (640, 480))
    hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
    #red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(img_resize, low_red, high_red)
    #red = cv2.bitwise_and(img_resize, img_resize, mask=red_mask)


    contours, hierarchy = cv2.findContours(red_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    def get_contour_areas(contours):
        all_areas = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            all_areas.append(area)
        return all_areas

    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
    largest_item = sorted_contours[0]
    cv2.drawContours(img_resize, largest_item, -1, (255, 0, 0), 10)

    cv2.imshow("img",img_resize)
    cv2.imshow("mask",red_mask)
    cv2.imshow('Largest Object', img_resize)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()