from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import cv2
import math as m

#aaa="t1d"#more shape than color but if masteris disapper
#aaa="kcf"#shape and position sometime just disappear
aaa="csrt"#position sometime overlap
#aaa="boosting"#shape but object cannot disapper
#aaa="mil"#shape but object cannot disapper
#aaa="medianflow"#shape but object cannot disapper
# extract the OpenCV version info
(major, minor) = cv2.__version__.split(".")[:2]
# if we are using OpenCV 3.2 OR BEFORE, we can use a special
# factory function to create our object tracker
if int(major) == 3 and int(minor)<3:
tracker = cv2.TrackerTLD_create()
# otherwise, for OpenCV 3.3 OR NEWER, we need to explicity
# call the approrpiate object tracker constructor:
else:
# initialize a dictionary that maps strings to their
# corresponding OpenCV object tracker implementations
OPENCV_OBJECT_TRACKERS ={
"t1d":cv2.TrackerTLD_create(),
"csrt":cv2.TrackerCSRT_create(),
"kcf":cv2.TrackerKCF_create(),
"boosting":cv2.TrackerBoosting_create(),
"mil":cv2.TrackerMIL_create(),
"medianflow":cv2.TrackerMedianFlow_create(),
}
# grab the appropriate object tracker using our dictionary of
# OpenCV object tracker objects
tracker = OPENCV_OBJECT_TRACKERS[aaa]
# initialize the bounding box coordinates of the object
# we are going to track
initBB = None

#open the camera and start the video
print("starting video stream..." )
vs = VideoStream(0).start()
time.sleep(1.0)
# initialize the FPS throughput estimator
fps=None

# loop over frames from the video stream
while True:
# grab the current frame, then handle if we are using a
# VideoStream or VideoCapture object
frame = vs.read()
frame = imutils.rotate(frame, 0)
# check to see if we have reached the end of the stream
if frame is None:
break
# resize the frame (so we can process it faster) and grab the
# frame dimensions
frame = imutils.resize(frame,width =480)
(H,W) = frame.shape[:2]

if initBB is not None:
# grab the new bounding box coordinates of the object
(success,box) = tracker.update(frame)
# check to see if the tracking was a success
if success:
(x,y,w,h) =[int(v) for v in box]
cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
print("x",x,"y",y,"w",w,"h",h)
#calculate the angle of rotation
angle = m.atan(((x+(w/2))-162)/(324-(y+(h/2))))
ang = (180/3.14)*angle
#the area where the arm grib objec
if((x-w/2)**2)+((y-h)**2==(80**2((:
f= open('E:phase\\phase.xlsx','w')
print("angle",ang
)
f.write(ang
)
f.close()
# update the FPS counter
fps.update()
fps.stop()

if initBB is not None:
# grab the new bounding box coordinates of the object
(success,box) = tracker.update(frame)
# check to see if the tracking was a success
if success:
(x,y,w,h) =[int(v) for v in box]
cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
print("x",x,"y",y,"w",w,"h",h)
#calculate the angle of rotation
angle = m.atan(((x+(w/2))-162)/(324-(y+(h/2))))
ang = (180/3.14)*angle
#the area where the arm grib objec
if((x-w/2)**2)+((y-h)**2==(80**2((:
f= open('E:phase\\phase.xlsx','w')
print("angle",ang
)
f.write(ang
)
f.close()
# update the FPS counter
fps.update()
fps.stop()

# if the 's' key is selected, we are going to "select"
# a bounding box to track
if key == ord("s"):
# select the bounding box of the object we want to track (make
# sure you press ENTER or SPACE after selecting the ROI)
initBB=cv2.selectROI("Frame", frame)
# start OpenCV object tracker using the supplied bounding box
# coordinates, then start the FPS throughput estimator as well
tracker.init(frame,initBB)
fps = FPS().start()
# if the `q` key was pressed, break from the loop
if key == ord("q"):
break
# close all windows
cv2.destroyAllWindows()
print("End")
     
     
     
     
    

