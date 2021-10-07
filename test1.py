import cv2
import numpy as np
from pyzbar.pyzbar import decode
from playsound import playsound

#timer = cv2.getTickCount()
#success, img = cap.read()

cap = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create()
success , img = cap.read()
bbox = cv2.selectROI( "TRACKING PROJECT", img , False)
tracker.init(img , bbox)
#cap.set(10,1000)
def code():
 #   cap.set(3, 640)
  #  cap.set(4, 480)
    with open('myfile.text') as f:
        mydatalist = f.read().splitlines()
#    while True:
 #       success, img = cap.read()
        for i in decode(img):
            # print(i.data)
            mydata = i.data.decode('utf-8')
            print(mydata)
            if mydata in mydatalist:
                cv2.putText(img, "Authorized", (75, 105), cv2.FONT_ITALIC, 0.7, (1, 255, 1), 3, 1)
            #    playsound('alert.mp3')
            else:
                cv2.putText(img, "Un-Authorized", (75, 105), cv2.FONT_ITALIC, 0.7, (2, 255, 2), 3, 1)
             #   playsound('alarm.mp3')
            pts = np.array([i.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 255, 0), 5)
#        cv2.imshow('Result', img)
#        cv2.waitKey(1)



#tracker = cv2.TrackerMOSSE_create()
#tracker = cv2.TrackerKCF_create()


def tracks(img , bbox):
    x,y,w,h = int(bbox[0]) , int(bbox[1]) , int(bbox[2]) , int(bbox[3])
    cv2.rectangle(img , (x , y) ,((x+w) , (y+h)) , (255,0,255) , 3 , 1)
    cv2.putText(img , "tracking" , (75 , 75) , cv2.FONT_ITALIC , 0.7 , (1,255,1) , 3 , 1)
    code()

while True:
    timer = cv2.getTickCount()
    success , img = cap.read()
    success , bbox = tracker.update(img)
    if success:
        tracks(img,bbox)
     #   code()
    else:
        cv2.putText(img , "NOT TRACK" , (75,20) , cv2.FONT_ITALIC , 0.7 , (0,255,0) , 2)
    #cv2.imshow("PROJECT", img)
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img , str(int(fps)) , (75,50) , cv2.FONT_ITALIC , 0.7 , (0,2,255) , 2)
    cv2.imshow("TRACKING" , img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break