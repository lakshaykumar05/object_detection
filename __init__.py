import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
#with open('Authentication.txt') as f:
 #   auth_list = f.read().splitlines()
while True:
    success, img = cap.read()
    for i in decode(img):
        myData = i.data.decode('utf-8')
      #  pts2 = np.array([i.polygon],np.int32)
       # pts2 = pts2.reshape(-1,1,2)
   #     if myData in auth_list:
    #        x = 'Authorised'
     #       mycolor = (0, 255, 0)
      #      cv2.putText(img, x, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, mycolor(), 2)
   #     else:
    #        x = 'Un-authorised'
        mycolor = (0, 0, 255)
        x = "hello"
        pts2 = i.rect
        cv2.putText(img, x, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, mycolor(), 2)
        pts = np.array([i.polygon], np.int32)
        pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = i.rect

    cv2.imshow('Result', img)
    cv2.waitKey(1)