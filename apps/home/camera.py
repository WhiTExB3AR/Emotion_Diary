# ------- Start: B3AR config code -------
# import the necessary packages
import cv2
import os

class VideoCamera(object):
    def __init__(self):
        #capturing video
        self.camera = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.camera.release()

#make shots directory to save pics
try:
    os.mkdir('./snapshots')
except OSError as error:
    pass

def gen_frames(self):  # generate frame by frame from camera
   while True:
        # initialize the video stream and allow the camera sensor to warm up
        #extracting frames
        success, frame = self.camera.read()  # read the camera frame
        if not success:
            break
        else:
            # print("[INFO] loading face detector...") # face detection
            # detector = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
            # faces = detector.detectMultiScale(frame,1.1,7)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #  # Draw the rectangle around each face
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # encode OpenCV raw frame to jpg and displaying it
            ret, jpeg = cv2.imencode('.jpg', frame) 
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# ------- End: B3AR config code -------