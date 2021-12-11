# -*- encoding: utf-8 -*-

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

# ------- Start: B3AR config code -------
from flask import Response
from apps.home.camera import gen_frames

# ------- End: B3AR config code -------

@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

# ------- Start: B3AR config code -------
# @blueprint.route('/video_feed')
def video_feed():

    res = Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return res
# ------- End: B3AR config code -------

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
