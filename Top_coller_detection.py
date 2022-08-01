import cv2
import numpy as np

def nothing (x):
    pass

#cap = cv2.VideoCapture('fire.mp4')
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H","Trackbars",0,255, nothing)
cv2.createTrackbar("L-S","Trackbars",0,255, nothing)
cv2.createTrackbar("L-V","Trackbars",0,255, nothing)
cv2.createTrackbar("U-H","Trackbars",171,171, nothing)
cv2.createTrackbar("U-S","Trackbars",255,255, nothing)
cv2.createTrackbar("U-V","Trackbars",255,255, nothing)

while True:
    #_, img1 = cap.read()
    img = cv2.imread('Asphalt2.jpeg')
    img1 = cv2.resize(img,(640,480))
    hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H","Trackbars")
    l_s = cv2.getTrackbarPos("L-S","Trackbars")
    l_v = cv2.getTrackbarPos("L-V","Trackbars")
    u_h = cv2.getTrackbarPos("U-H","Trackbars")
    u_s = cv2.getTrackbarPos("U-S","Trackbars")
    u_v = cv2.getTrackbarPos("U-V","Trackbars")


    lower_red = np.array([l_h,l_s,40])
    higher_red = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,lower_red,higher_red)
    #remove unnecessary noise from mak
    kernel = np.ones ((30,30),np.uint8)
    mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)


    image_binary = cv2.inRange(hsv, lower_red, higher_red)
    check_if_fire_detected = cv2.countNonZero(image_binary)
    print(int(check_if_fire_detected))
    if int(check_if_fire_detected) >= 10000:
        cv2.putText(img1, "Fire Detected !", (100, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


    cv2.imshow("frame1",img1)
    cv2.imshow("frame2",mask)
    #cv2.imshow("image_binary",image_binary)


    key = cv2.waitKey(1)
    if key == 27:
        break

#cap.release()
cv2.destroyAllWindows()