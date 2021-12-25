# -*- encoding: utf-8 -*-

from flask_wtf import form
import apps
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

# ------- Start: B3AR config code -------
from flask import Response, redirect, url_for, flash
from flask_login import (
    current_user
)
from apps import db
from apps.authentication.models import Users, Diaries, Emotions
from apps.home.camera import gen_frames
from apps.home.forms import CreateForm, ViewForm
import datetime
import pytz # libraby for python timezone
import werkzeug
import io
from werkzeug.utils import secure_filename

from PIL import Image
import cv2
import numpy as np
import os
from apps.fer_model.predict import transform_image, res_solver, model_options
# ------- End: B3AR config code -------

@blueprint.route('/index')
@login_required
def index():

    # ------- Start: B3AR config code -------
    create_form = CreateForm(request.form)
    view_form = ViewForm(request.form)
    return render_template('home/index.html', segment='index', form=create_form)
    # ------- End: B3AR config code -------

    return render_template('home/index.html', segment='index')

# ------- Start: B3AR config code -------
# print(" * [INFO] Loading face detector...") # Load model haarcascade global -> load 1 times
# detector = cv2.CascadeClassifier('apps/static/assets/xml/haarcascade/haarcascade_frontalface_default.xml')

# @blueprint.route('/video_feed')
# def video_feed():

#     res = Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
#     return res

@blueprint.route('/newdiary', methods=['GET', 'POST'])
def new_diary():

    # create_form = CreateForm(request.form)

    post_datetime = request.form['post_datetime']
    uid = request.form['uid']
    eid = request.form['eid']
    imgname = request.form['imgname']
    title = request.form['title']
    content = request.form['content']
    if(post_datetime):
        post_datetime = datetime.datetime.strptime(post_datetime, '%Y-%m-%d %H:%M:%S.%f')
        diary = Diaries.query.filter_by(post_datetime=post_datetime).first()
        if diary:
            return render_template(
                'home/newdiary.html',
                msg="Please write new diary",
                success=False,
                segment='newdiary',
                # form=create_form
            )
        # diary = Diaries(**request.form)
        diary = Diaries(
            post_datetime = post_datetime,
            uid = uid,
            eid = eid,
            imgname = imgname,
            title = title, 
            content = content
        )
        db.session.add(diary)
        db.session.commit()
        print('* [INFO] Added to DB:', '\n** Datetime: ', post_datetime, '\n** User ID: ', uid, '\n** Emotion ID: ', eid, '\n** Image Name: ', imgname, '\n** Title: ', title, '\n** Content: ', content)

        # file=request.files['file']
        # file.save(f'apps/static/assets/img/{imgname}')
        return render_template(
            'home/newdiary.html',
            success=True,
            segment='newdiary',
            # form=create_form
        )
        # return {
        #     'result':True
        # }
    return render_template(
        'home/newdiary.html',
        segment='newdiary',
        # form=create_form
    )
# ------- End: B3AR config code -------

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
        # ------- Start: Crop face -------
        # upload_image= Image.open(file)
        # image_1 = face_detected(upload_image)

        # rgb_image=image_1.convert('RGB')
        # l_image=image_1.convert('L')

        print('File:', file)

        imagefile_name=file.filename # get the filename of image in FileStorage
        snapshots_path='apps/static/assets/img/snapshots' # path to save image
        file.save(os.path.join(snapshots_path, secure_filename(imagefile_name))) # save image
        print('* [INFO] Successfully saved image')

        rgb_image=Image.open(file).convert('RGB')
        l_image=Image.open(file).convert('L')
        # ------- End: Crop face -------
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
