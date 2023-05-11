#Haar cascade feature detector #2
#Custom made Haar Cascade XML file!

import cv2
import time

# MUST USE THE FOLLOWING FILES: vid01.mp4 & cascade4.xml
orange_classifier = cv2.CascadeClassifier('orange detector/xml/cascade4.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('orange detector/mp4/vid01.mp4')

# Loop once video is successfully loaded
while cap.isOpened():
    
    time.sleep(1/60)
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB) #It should be cv2.COLOR_BGR2GRAY, but it's hard to fine-tune and I don't know why!

    orange = orange_classifier.detectMultiScale(gray,scaleFactor=8.85,minSize=(290,290), maxSize=(320,320),minNeighbors=18,flags=cv2.CASCADE_SCALE_IMAGE)

    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in orange:
        image = cv2.rectangle(frame, (x-300,y-80), ((x+w-150), (y+h+150)), (0, 255, 0), 3)
        cv2.putText(image,'Orange', (x+220,y-75), cv2.FONT_ITALIC, 0.85, (0,140,255),2)
        cv2.imshow('Fresh Oranges', frame)

    if cv2.waitKey(1)== 13: #is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()