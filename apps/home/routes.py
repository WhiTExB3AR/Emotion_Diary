# -*- encoding: utf-8 -*-

from flask_wtf import form
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

# ------- Start: B3AR config code -------
from flask import Response, redirect, url_for, flash
from apps import db
from apps.authentication.models import Users, Diaries, Emotions
from apps.home.camera import gen_frames
from apps.home.forms import CreateForm, ViewForm
import datetime
import pytz # libraby for python timezone
from werkzeug.utils import secure_filename

from PIL import Image
import cv2
from apps.fer_model.predict import transform_image, res_solver, model_options
# ------- End: B3AR config code -------

@blueprint.route('/index')
@login_required
def index():
    create_form = CreateForm(request.form)
    view_form = ViewForm(request.form)
    return render_template('home/index.html', segment='index', form=create_form)

# ------- Start: B3AR config code -------
print(" * [INFO] Loading face detector...") # Load model haarcascade global -> load 1 times
detector = cv2.CascadeClassifier('apps/static/assets/xml/haarcascade/haarcascade_frontalface_default.xml')

# @blueprint.route('/video_feed')
# def video_feed():

#     res = Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
#     return res

@blueprint.route('/new_diary', methods=['GET', 'POST'])
def new_diary():
    post_datetime = None
    # validate form
    if form.validate_on_submit():
        post_datetime = form.post_datetime.data
        form.post_datetime.data = datetime.now(pytz.timezone('Asia/Saigon')) # 'Etc/GMT+7'
        fmt = '%Y-%m-%d %H:%M:%S'



    return render_template('home/index.html', 
                            # post_datetime = post_datetime, 
                            form = form)

    # create_new_diary = CreateForm(request.form)
    # if 'new_diary' in request.form:
    #     # read form data
    #     post_datetime = request.form['post_create_datetime']
    #     emoname = request.form['emoname']
    #     title = request.form['title']
    #     content = request.form['content']

    #     # create the diary
    #     diary = Diaries(**request.form)
    #     db.session.add(diary)
    #     db.session.commit()

    #     return render_template('home/diary.html',
    #                             msg='Diary of today was recorded',
    #                             segment = 'new_diary', 
    #                             success=True,
    #                             form=create_new_diary)

    # else:
    #     return redirect(url_for('home_blueprint.index'))

# ------- End: B3AR config code -------

# @blueprint.route('/handle_image', methods=['POST'])

# def face_detect(): # chưa config xong
#     # load the input image from disk, resize it, and convert it to
#     # grayscale
#     image_org = cv2.imread(args["image"])
#     # image_resize = imutils.resize(image_org, width=500)
#     gray = cv2.cvtColor(image_org, cv2.COLOR_BGR2GRAY)

#     # detect faces in the input image using the haar cascade face
#     # detector
#     print("[INFO] performing face detection...")
#     faces_result = detector.detectMultiScale(
#         gray, 
#         scaleFactor = 1.05,
#         minNeighbors = 25, 
#         minSize = (30, 30),
#         flags = cv2.CASCADE_SCALE_IMAGE)
#     print("[INFO] {} faces detected...".format(len(faces_result)))
#     count = 0
#     for i in range(len(faces_result)):
#         count = count + 1


#     # loop over the bounding boxes
#     for (x, y, w, h) in faces_result:
#         # draw the face bounding box on the image (B, G, R) = (255, 0, 0) => box line is blue
#         cv2.rectangle(image_org, (x, y), (x + w, y + h), (0,155,255), 2)

#     # print("width: {} pixels".format(w))
#     # print("height: {}  pixels".format(h))

#     # ------- Start: split to file name -------
#     file_name_pathlib = Path(args["image"]).stem
#     print("Got the file name original: ", file_name_pathlib)

#     # Save the image with rectangle face detection
#     cv2.imwrite('images/results/detected_rectangle/' + 
#                 "Face Detected HAAR_" + 
#                 str(file_name_pathlib) + 
#                 ".png", 
#                 image_org)
#     print('=> Successfully saved face detection rectangle and show each face now')

#     # ------- Start: Crop face -------
#     # 1. using OpenCV
#     i = 0 # for each face focus
#     for (x, y, w, h) in faces_result:
#         print(x,y,w,h)
#         crop_face = gray[y:y+h, x:x+w]
#         cv2.imwrite('images/results/face_focus/haar/' +
#                     str(file_name_pathlib) +
#                     # 'HAAR_face_' +
#                     # str(i) +
#                     '.png', 
#                     crop_face)
#         cv2.imshow("Cropped face.png", crop_face)
#         i = i + 1
#         count = count - 1
#         if (count < 0): # no face focus found in len(faces_result)
#             break
#         cv2.waitKey(0)
    # ------- End: Crop face -------

    # show the output image
    # cv2.imshow("Image", image)
    # path = 'images/results/face_detected'
    # cv2.imwrite(os.path.join(path,"Face detected Haar.png", image_org))
    # print('Successfully saved and show now')
    # cv2.imshow("Face detected Haar.png", image_org)
    # cv2.waitKey(0)



@blueprint.route('/handle_image', methods=['POST'])
def handle_image():
    if 'file' not in request.files:
        return 'no file'
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return 'file empty'
    if file:
        print('File:', file)
        rgb_image=Image.open(file).convert('RGB')
        l_image=Image.open(file).convert('L')
        rgb_img = transform_image(rgb_image).unsqueeze(0)
        l_img=transform_image(l_image).unsqueeze(0)
        batch={
            'img_tensor': rgb_img,
            'img_tensor_gray': l_img,
            'img_res_tensor': l_img,
            'img_path': 'flask'
        }

        rs=res_solver.test_networks(model_options, batch)

        return {
            'predicted_label':rs.tolist()[0]
        }


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            pass

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
