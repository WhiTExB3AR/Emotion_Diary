# -*- encoding: utf-8 -*-

import flask_login
from flask_wtf import form
import apps
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

# ------- Start: B3AR config code -------
from flask import Response, redirect, url_for, flash, jsonify
from flask_login import (
    current_user
)
from apps import db, login_manager
from apps.authentication.models import Users, Diaries, Emotions
from apps.home.camera import gen_frames
from apps.home.forms import CreateForm, UpdateForm
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
from sqlalchemy import func
# ------- End: B3AR config code -------

@blueprint.route('/index')
@login_required
def index():

    # ------- Start: B3AR config code -------
    create_form = CreateForm(request.form)
    update_form = UpdateForm(request.form)
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
            'home/ui-view-diary.html',
            success=True,
            segment='ui-view-diary',
            # form=create_form
        )
        # return {
        #     'result':True
        # }
    return render_template(
        'home/ui-view-diary.html',
        segment='ui-view-diary',
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

@blueprint.route('/fetch_diary', methods=['POST'])
def fetch_diary():
    uid=current_user.get_id()
    # query DB
    diaries=Diaries.query.filter(Diaries.uid==uid).all()
    result=[]
    for d in diaries:
        result.append({
            'title':d.title,
            'content':d.content,
            'id':d.id,
            'post_datetime':d.post_datetime.isoformat(),
            'eid':d.eid,
            'imgname':d.imgname
        })

    return jsonify(result=result)

    # {
    #     "result":[
    #         {},{},{}
    #     ]
    # }
    # response.result
@blueprint.route('/fetch_chart', methods=['POST'])
def fetch_chart():
    
    # uid=current_user.get_id()

    if(current_user):
    # only_uid = Diaries.query.filter_by(uid=uid).first()
        ueid=current_user.query\
            .join(Diaries).join(Emotions)\
            .add_columns(Users.id, Diaries.eid, Emotions.emoname, func.count(Diaries.eid))\
            .filter(Diaries.uid==current_user.get_id())\
            .group_by(Diaries.eid)\
            .all()
        # ueid=db.session.query(Users, Diaries, Emotions, func.count(Diaries.eid)).join(Diaries).join(Emotions).filter(Diaries.uid==uid).group_by(Diaries.uid, Diaries.eid, Emotions.emoname).all()

    # ueid=db.session.query(Users.id, Diaries.eid, Emotions.emoname, func.count(Diaries.eid)).outerjoin(Diaries, Users.id==Diaries.uid).outerjoin(Emotions, Diaries.eid==Emotions.id).group_by(Users.id, Diaries.eid, Emotions.emoname).all()
    # diaries=db.session.query(Diaries.eid, func.count(Diaries.eid)).group_by(Diaries.eid).all()
    result=[]
    for d in ueid:
        result.append({
            'uid': d[1],
            'eid': d[2],
            'emoname': d[3],
            'count': d[4]
        })
    return jsonify(result=result)

@blueprint.route('/fetch_week', methods=['POST'])
def fetch_weekly():
    str_date=request.form.get('datetime',None)
    if str_date:
        current_date=datetime.datetime.fromisoformat(str_date)
    else:
        current_date=datetime.datetime.now()
    current_date = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date=current_date - datetime.timedelta(days=current_date.weekday())
    end_date=start_date+datetime.timedelta(days=7)
    diaries=Diaries.query\
        .filter(Diaries.uid==current_user.get_id())\
        .filter(Diaries.post_datetime.between(start_date,end_date))\
        .all()
        # .filter(and_(
        #     Diaries.uid == 5,
        #     Diaries.post_datetime.between(start_date,end_date)
        # ))\
        # .all()
        # .order_by(Diaries.post_datetime.desc())\
        # .all()
    diary_stats=dict()
    for i in range(7):
        diary_stats[i]=-1
    for d in diaries:
        post_day_of_week=d.post_datetime.weekday()
        diary_stats[post_day_of_week]=d.eid
        # result.append({
        #     'post_datetime':d.post_datetime.isoformat(),
        #     'eid':d.eid,
        # })
    return diary_stats

@blueprint.route('/update-diary', methods=['POST'])
def update_diary():

    # create_form = CreateForm(request.form)

    did = request.form['did']
    title = request.form['title']
    content = request.form['content']

    uid=current_user.get_id()
    # query DB
    diary=Diaries.query.get(did)
    diary.title = title
    diary.content = content
    db.session.commit()
    return {
        'result':'Updated successfully'
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
