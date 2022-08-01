import cv2
import numpy as np

def nothing (x):
    pass

cap = cv2.VideoCapture('redring.mp4')
#cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H","Trackbars",0,255, nothing)
cv2.createTrackbar("L-S","Trackbars",0,255, nothing)
cv2.createTrackbar("L-V","Trackbars",0,255, nothing)
cv2.createTrackbar("U-H","Trackbars",0,255, nothing)
cv2.createTrackbar("U-S","Trackbars",0,255, nothing)
cv2.createTrackbar("U-V","Trackbars",0,255, nothing)

while True:
    _, img = cap.read()
    #img = cv2.imread('frame125.jpg')
    img_resize = cv2.resize(img,(640,480))

    #cv2.rectangle(img_resize, pt1=(250, 180), pt2=(330, 300), color=(0, 0, 255), thickness=3)
    #cv2.rectangle(img_resize, pt1=(350, 180), pt2=(430, 300), color=(0, 0, 255), thickness=3)
    roi = img_resize[180:300, 250:330]
    #roi = img_resize[180:300, 350:430]
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H","Trackbars")
    l_s = cv2.getTrackbarPos("L-S","Trackbars")
    l_v = cv2.getTrackbarPos("L-V","Trackbars")
    u_h = cv2.getTrackbarPos("U-H","Trackbars")
    u_s = cv2.getTrackbarPos("U-S","Trackbars")
    u_v = cv2.getTrackbarPos("U-V","Trackbars")


    lower_red = np.array([0,0,0])
    higher_red = np.array([174,235,255])

    red_mask = cv2.inRange(hsv,lower_red,higher_red)
    _, mask1 = cv2.threshold(red_mask, 254, 255, cv2.THRESH_BINARY)

    contours, h = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        cnt = contours[len(contours) - 1]
        cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
    print(str(len(contours)))
    for c in contours:
        x = 6000.0
        if cv2.contourArea(c) > x:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 3)


    cv2.imshow("frame1",img_resize)
    cv2.imshow("frame2",red_mask)
    cv2.imshow("frame3", roi)
    #cv2.imshow("image_binary",image_binary)

    key = cv2.waitKey(1000)
    if key == 27:
        break

#cap.release()
cv2.destroyAllWindows()