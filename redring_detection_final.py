import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture('redring.mp4')

myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 120, 'smin': 61, 'vmin': 55, 'hmax': 179, 'smax': 255, 'vmax': 255}


while True:
    success,img = cap.read()
    #img = cv2.imread('frame125.jpg')
    img_crop = img[120:250, 230:380]

    imgColor,mask = myColorFinder.update(img_crop,hsvVals)
    #find locatoin of the ball
    imgContours,Contours = cvzone.findContours(img_crop,mask,minArea=200)
    if Contours:
        cx,cy = Contours[0]['center']
        print(cx+cy)
        cv2.circle(imgContours,(cx,cy),5,(0,255,0),cv2.FILLED)
        if (cx+cy)>80:
            print('ok')
        else:
            print('rejected')

    img_final = cv2.resize(imgContours,(0,0),None,0.7,0.7)
    cv2.imshow("image1", img)
    cv2.imshow("imgColor",imgContours)
    cv2.imshow("imgmask", mask)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
