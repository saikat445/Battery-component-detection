import cv2
import numpy as np

def nothing (x):
    pass

cap = cv2.VideoCapture('redring.mp4')
#cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H","Trackbars",0,255, nothing)
cv2.createTrackbar("L-S","Trackbars",0,255, nothing)
cv2.createTrackbar("L-V","Trackbars",0,255, nothing)
cv2.createTrackbar("U-H","Trackbars",180,180, nothing)
cv2.createTrackbar("U-S","Trackbars",255,255, nothing)
cv2.createTrackbar("U-V","Trackbars",255,255, nothing)

while True:
    _, img = cap.read()
    #img = cv2.imread('frame125.jpg')
    img_resiged = img[100:220, 350:470]
    #roi = img1[180:300, 350:430]
    hsv = cv2.cvtColor(img_resiged,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H","Trackbars")
    l_s = cv2.getTrackbarPos("L-S","Trackbars")
    l_v = cv2.getTrackbarPos("L-V","Trackbars")
    u_h = cv2.getTrackbarPos("U-H","Trackbars")
    u_s = cv2.getTrackbarPos("U-S","Trackbars")
    u_v = cv2.getTrackbarPos("U-V","Trackbars")


    lower_red = np.array([0,0,0])
    higher_red = np.array([174,235,255])


    mask = cv2.inRange(hsv,lower_red,higher_red)
    image_binary = cv2.inRange(hsv, lower_red, higher_red)
    check_if_fire_detected = cv2.countNonZero(image_binary)
    print(int(check_if_fire_detected))
    if int(check_if_fire_detected) >= 10000:
        cv2.putText(img, "Fire Detected !", (100, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


    cv2.imshow("frame1",img)
    cv2.imshow("frame2",img_resiged)
    cv2.imshow("image_binary",mask)


    key = cv2.waitKey(500)
    if key == 27:
        break

#cap.release()
cv2.destroyAllWindows()