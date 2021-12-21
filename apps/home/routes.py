# -*- encoding: utf-8 -*-

from flask_wtf import form
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

# ------- Start: B3AR config code -------
from flask import Response, redirect, url_form, flash
from apps import db
from apps.authentication.models import Users, Diaries, Emotions
from apps.home.camera import gen_frames
from apps.home.forms import CreateForm, ViewForm
import datetime
import pytz # libraby for python timezone
from werkzeug.utils import secure_filename

from PIL import Image
from apps.fer_model.predict import transform_image, res_solver, model_options
# ------- End: B3AR config code -------

@blueprint.route('/index')
@login_required
def index():
    create_form = CreateForm(request.form)
    view_form = ViewForm(request.form)
    return render_template('home/index.html', segment='index', form=create_form)

# ------- Start: B3AR config code -------
@blueprint.route('/video_feed')
def video_feed():

    res = Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return res

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

@blueprint.route('/handle_image',methods=['POST'])
def handle_image():
    if 'file' not in request.files:
        return 'no file'
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return 'file empty'
    if file:
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
            'result':rs.tolist()
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
