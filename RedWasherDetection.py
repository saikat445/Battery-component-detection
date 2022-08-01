import cv2
import cvzone
from cvzone.ColorModule import  ColorFinder
import numpy as np

cap = cv2.VideoCapture(0)

myColorFinder= ColorFinder(False)
hsvVals = {'hmin': 22, 'smin': 0, 'vmin': 0, 'hmax': 167, 'smax': 255, 'vmax': 255}

while True:
    success, img = cap.read()
    #img = cv2.imread('2.jpeg')
    #img= img[0:900, :]
    img_resize = cv2.resize(img,(640,480))
    roi = img_resize[150:300, 200:300]
    cv2.rectangle(img_resize, (200,150),(300,300),(0,255,0), 5)
    #cv2.rectangle(img_resize,height,width,(0,0,255),thickness=4)

    # find color ball
    imgColor, mask = myColorFinder.update(roi,hsvVals)
    kernel = np.ones((10, 10), np.uint8)
    mask = cv2.erode(mask, kernel)
    contour, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area >900:
            #cv2.drawContours(img_resize,[cnt],0,(0,255,0),4)
            print(area)
            cv2.putText(img_resize,str(area),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv2.LINE_AA)

        #start_point = [0, 0]
        #end_point = [10, 10]
        #cv2.rectangle(imgContours, tuple(start_point), tuple(end_point), (0,255,0), thickness=1

        #cv2.rectangle(imgContours,cx,cy,(0,255,0),thickness=4,lineType=None)

    # Display

    cv2.imshow("image", img_resize)
    cv2.imshow("mask",mask)
    cv2.imshow("roi",roi)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
