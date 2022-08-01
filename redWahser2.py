import cv2
import cvzone
from cvzone.ColorModule import  ColorFinder
import numpy as np

cap = cv2.VideoCapture("2.jpeg")

myColorFinder= ColorFinder(False)
hsvVals = {'hmin': 12, 'smin': 0, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}


while True:
    success, img = cap.read()
    img = cv2.imread('2.jpeg')
    #img= img[0:900, :]
    img_resize = cv2.resize(img,(640,480))
    areaArray = []
    conunt = 1


    # find color ball
    imgColor, mask = myColorFinder.update(img_resize,hsvVals)

    contour, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i, c in enumerate(contour):
        area = cv2.contourArea(c)
        areaArray.append(area)
        sorteddata = sorted(zip(areaArray, contour), key=lambda x: x[0], reverse=True)
        secondlargestcontour = sorteddata[1][1]
        x, y, w, h = cv2.boundingRect(secondlargestcontour)
        cv2.drawContours(img_resize, secondlargestcontour, -1, (255, 0, 0), 2)
        cv2.rectangle(img_resize, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #start_point = [0, 0]
        #end_point = [10, 10]
        #cv2.rectangle(imgContours, tuple(start_point), tuple(end_point), (0,255,0), thickness=1

        #cv2.rectangle(imgContours,cx,cy,(0,255,0),thickness=4,lineType=None)

    # Display

    cv2.imshow("image", img_resize)
    cv2.imshow("mask",mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
