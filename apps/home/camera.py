# ------- Start: B3AR config code -------
import cv2
import imutils
from imutils.video import VideoStream
import argparse
import datetime, time
import os, sys
import numpy as np

camera = cv2.VideoCapture(0)

#make shots directory to save pics
try:
    os.mkdir('./snapshots')
except OSError as error:
    pass

def gen_frames():  # generate frame by frame from camera
   while True:
       # initialize the video stream and allow the camera sensor to warm up
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # print("[INFO] loading face detector...") # face detection
            # detector=os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
            # faces=detector.detectMultiScale(frame,1.1,7)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #  #Draw the rectangle around each face
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame) # load video streaming
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# ------- End: B3AR config code -------