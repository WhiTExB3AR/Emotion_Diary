# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

# create diary

class CreateForm(FlaskForm):
    post_datetime = TextField(
        'Date Time',
        id='post_create_datetime',
        validators=[DataRequired()]
    )
    uid = TextField(
        'User ID',
        id='user_create_diary',
        validators=[DataRequired()]
    )
    eid = TextField(
        'Mood today',
        id='eid_create_diary',
        validators=[DataRequired()]
    )
    imgname = TextField(
        'Image Name',
        id='img_create_diary',
        validators=[DataRequired()]
    )
    title = TextField(
        'Title',
        id='title_create_diary'
    )
    content = TextField(
        'Content',
        id='content_create_diary'
    )    


class UpdateForm(FlaskForm):
    diaryid = TextField(
        'Diary ID',
        id='did',
        validators=[DataRequired()]
    )
    title = TextField(
        'Title',
        id='title_update_diary'
    )
    content = TextAreaField(
        'Content',
        id='content_update_diary'
    )    


# ------- Start: B3AR config code -------

# ------- End: B3AR config code -------