# ------- Start: B3AR config code -------
# import the necessary packages
import cv2
import os

camera = cv2.VideoCapture(0)

# make shots directory to save pics
try:
    os.mkdir('./snapshots')
except OSError as error:
    pass

print(" * [INFO] Loading face detector...") # Load model haarcascade global -> load 1 times
detector = cv2.CascadeClassifier('apps/static/assets/xml/haarcascade/haarcascade_frontalface_default.xml')

def gen_frames():  # generate frame by frame from camera
   while True:
        # initialize the video stream and allow the camera sensor to warm up
        #extracting frames
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            
            # Move to line 15
            # with current_app.app_context():
            # detector = g.get('face_detector', None)
            # if not detector:

            faces = detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                # print("[INFO] Detected face...")
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
                crop_face = gray[y:y+h, x:x+w] # cut only face
            # # cut image
            # for (x, y, w, h) in faces:
            #     print(x,y,w,h)
            #     crop_face = gray[y:y+h, x:x+w]
            ####################################################################################################
            # encode OpenCV raw frame to jpg and displaying it
            ret, jpeg = cv2.imencode('.jpg', frame) 
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# ------- End: B3AR config code -------