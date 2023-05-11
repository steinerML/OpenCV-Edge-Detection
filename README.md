# OpenCV Feature Detection using Haar Cascade

In this short coding exercise I have used a basic feature of OpenCV that is mainly used for face detection but I applied it to something so simple as an orange just to see how the feature detection (if there are any in an orange besides an edge against a background) was doing. 

The method I used is the so-called haar cascade together with a Cascade Classifier (XML file) that I put together myself with a set of images (negative&positives) using [Cascade Trainer GUI.](https://amin-ahmadi.com/cascade-trainer-gui)

These are - in a nutshell - the main steps I took to put this small experiment together:

+ **Install Cascade Trainer GUI**
+ **Prepare 150 positive images & 300 negative images (Negative to Positive ratio 2:1)**
+ **Apply settings to Cascade Trainer** (see table below for details)
+ **Adjust scaleFactor()**
+ **Size Thresholding via minSize() and maxSize()**
+ **Set minNeighbors()**
+ **Overall checks**

![Source Image Sequence](general_1.gif)

## Contents :
Feature Detection is quite a tricky and challenging task, specially when you are using a cascade classifier that is meant to be used for face detection and yet you use it on such a simple object as an orange. Bear in mind that the haar cascade classifier is trying to detect features by means of swiping a 'blueprint' (see image below) that fits within its binary structure. Meaning, that all the pixels that fall in the white side of the blueprint together with the black pixels on the other side.

Below a summary of the main functions used with the haar cascade classifier:

| Function            |Action                                                                        |
|:--------------------|------------------------------------------------------------------------------|
|**cv2.CascadeClassifier()**|Import Cascade Classifier XML file|
|**cv2.VideoCapture()**   |Improve Detection via history & varThreshold.|
|**cv2.cvtColor()**|Draw rectangle based on contour.|
|**orange_classifier.detectMultiScale()**    | Initializes detection settings|
|**cv2.rectangle()**    | Add rectangle to detected feature.|
|**cv2.putText()**    | Add text with 'Orange' tag|

## Test Image used: 
### Negative images.

![Source Image Sequence.](negative.gif)

### Positive images:
![Source Image Sequence.](positive.gif)

## Issues:
Several issues around the detection and tracking algorithm can be spotted if we take a closer look at some of the screenshots provided.
Most of the issues are related with:

+ Camera Instability.
+ Lighting Granularity.
+ Shade Inconsistency.
+ Poor Colour Thresholding.

![Source Image Sequence](general.gif)

## Summary:

```python
# Create object detector via a mask
object_detector = cv2.createBackgroundSubtractorMOG2()
```
```python
# Create object detector (improved with parameters)
cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=10)
```
```python
# Find contours of the objects in the mask
cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
```
```python
# Calculate area delimited by the contours (so we can impose a conditional later)
cv2.drawContours(roi,[cnt], -1, (0,255,0), 2)
```
```python
# Define Region of Interest (ROI)
roi = frame[340:720,500:800]
```
```python
#Apply the mask to ROI
object_detector.apply(roi)
```
```python
#Apply the mask to frame
object_detector.apply(frame)
```
```python
#Extract coordinates from contours
contours, _ = cv2.Contours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
```
```python
#Calculate area of contours
area = cv2.contourArea(cnt)
```
```python
#Define Region of Interest (ROI)
roi = frame[340:720,500:800]
```
```python
#Apply mask to ROI
mask = object_detector.apply(roi)
```
```python
#Improved detection via parameters!
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=80)
```
```python
#Draw rectangle based on contours
x,y,w,h = cv2.boundingRect(cnt)
```
```python
#Apply threshold to mask
 _, mask = cv2.threshold(mask, 254,255,cv2.THRESH_BINARY)
```
```python
#Create object tracker
tracker = EuclideanDistTracker()
```
```python
#Define empty list for object detection coordinates.
detections = []
```
```python
#Append coordinates to list
detections.append([x,y,w,h])
```
```python
#Update detections with box id
box_id = tracker.update(detections)
```
```python
#Add text (id number)
cv2.putText(roi,str(id), (x,y - 15),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,255),1)
```
```python
#Draw rectangle
cv2.rectangle(roi,(x,y),(x + w, y + h), (0,255,0), 3)
```
```python
#Print all windows (Source, Mask, ROI)
cv2.imshow("Frame", frame)
cv2.imshow("Mask", mask)
cv2.imshow("ROI", roi)
```

