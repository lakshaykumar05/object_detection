import cv2
import numpy as np
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('myfile.text') as f:
    mydatalist = f.read().splitlines()

while True:
    success , img = cap.read()
    for i in decode(img):
        #print(i.data)
        mydata = i.data.decode('utf-8')
        print(mydata)
        if mydata in mydatalist:
            cv2.putText(img, "Authorized", (75, 105), cv2.FONT_ITALIC, 0.7, (1, 255, 1), 3, 1)
        else:
            cv2.putText(img, "Un-Authorized", (75, 75), cv2.FONT_ITALIC, 0.7, (1, 255, 1), 3, 1)
        pts = np.array([i.polygon] , np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img , [pts] , True , (0,255,0) ,5)
    cv2.imshow('Result' , img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xff==ord('z'):
        break