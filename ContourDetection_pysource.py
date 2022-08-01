import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("L_H","Trackbar",0,180,nothing)
cv2.createTrackbar("L_S","Trackbar",0,255,nothing)
cv2.createTrackbar("L_V","Trackbar",0,255,nothing)
cv2.createTrackbar("U_H","Trackbar",179,179,nothing)
cv2.createTrackbar("U_S","Trackbar",155,155,nothing)
cv2.createTrackbar("U_V","Trackbar",238,238,nothing)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    L_H = cv2.getTrackbarPos("L_H","Trackbar")
    L_S = cv2.getTrackbarPos("L_S", "Trackbar")
    L_V = cv2.getTrackbarPos("L_V", "Trackbar")
    U_H = cv2.getTrackbarPos("U_H", "Trackbar")
    U_S = cv2.getTrackbarPos("U_S", "Trackbar")
    U_V = cv2.getTrackbarPos("U_V", "Trackbar")

    low_red = np.array([L_H,L_S,L_V])
    High_red = np.array([U_H,U_S,U_V])
    mask = cv2.inRange(hsv,low_red,High_red)
    kernel = np.ones((10,10),np.uint8)
    mask = cv2.erode(mask,kernel)

    contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1400:
            cv2.drawContours(frame,cnt,0,(0,255,0),5)

        #cv2.drawContours(frame,[cnt],0,(0,255,0),thickness=None)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap. release()
cv2.destroyAllWindows()



