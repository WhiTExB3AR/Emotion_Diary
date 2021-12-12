# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

# create diary

class CreateForm(FlaskForm):
    post_datetime = TextField('Date Time',
                                id='post_create_datetime',
                                validators=[DataRequired()])
    emoname = TextField('Mood today',
                         id='emotion_create_diary',
                         validators=[DataRequired()])
    title = TextField('Title',
                        id='title_create_diary')
    content = TextField('Content',
                    id='content_create_diary')    


class ViewForm(FlaskForm):
    post_datetime = DateTimeField('Date',
                                id='post_view_datetime',
                                validators=[DataRequired()])
    emoname = TextField('Mood Today',
                         id='today_view_emotion',
                         validators=[DataRequired()])
    title = TextField('Title',
                        id='title_view_diary')
    content = TextAreaField('Content',
                    id='content_view_diary')    


# ------- Start: B3AR config code -------

# ------- End: B3AR config code -------