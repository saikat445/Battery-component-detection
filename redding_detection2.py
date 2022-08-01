import cv2
import cvzone
from cvzone.ColorModule import  ColorFinder

cap = cv2.VideoCapture('frame125.jpeg')

myColorFinder= ColorFinder(False)
hsvVals = {'hmin': 0, 'smin': 0, 'vmin': 0, 'hmax': 179, 'smax': 97, 'vmax': 255}


while True:
    success, img = cap.read()
    img = cv2.imread('frame125.jpg')
    img_resize = cv2.resize(img,(640,480))
    cv2.rectangle(img_resize, pt1=(300, 180), pt2=(380, 300), color=(0, 0, 255), thickness=3)
    #cv2.rectangle(img_resize, pt1=(240, 180), pt2=(310, 300), color=(0, 0, 255), thickness=3)
    roi = img_resize[180:300, 240:310]

    # find color ball
    imgColor,mask = myColorFinder.update(roi,hsvVals)
    mask_image = cv2.countNonZero(mask)
    print(mask_image)


    # Display
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow("image", img_resize)
    cv2.imshow("imageColor",imgColor)
    cv2.imshow("image_roi", roi)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
