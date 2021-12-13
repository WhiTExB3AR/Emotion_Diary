# -*- encoding: utf-8 -*-

from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

# ------- Start: B3AR config code -------
from sqlalchemy.orm import relationship
from datetime import datetime
# ------- End: B3AR config code -------

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

    # ------- Start: B3AR config code -------
    post = db.relationship("Diaries", backref="author", lazy="dynamic") #lazy=true là chưa được vì chưa có dữ liệu trogn table
    # ------- End: B3AR config code -------

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

# ------- Start: B3AR config code -------
# Diary Table (many to one with user and emotion tables) => choosen relation code in diary table
class Diaries(db.Model):

    __tablename__ = "Diaries"

    id = db.Column(db.Integer, primary_key=True)
    post_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    uid = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    eid = db.Column(db.Integer, db.ForeignKey("Emotions.id"), nullable=False)
    imgname = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(128))
    contents = db.Column(db.String(255))

    def __init__(self, id ,uid, eid, title, imgname, contents):
        self.id = id
        self.uid = uid
        self.eid = eid
        self.imgname = imgname
        self.title = title
        self.contents = contents

    def __repr__(self):
        return str(self.id, self.post_datetime, self.uid, self.eid, self.imgname, self.title ,self.contents)

# Emotion Table
class Emotions(db.Model):

    __tablename__ = 'Emotions'

    id = db.Column(db.Integer, primary_key=True)
    emoname = db.Column(db.String(10), unique=True)
    emo_post = db.relationship("Diaries", backref="emopost", lazy="dynamic") #lazy=true là chưa được vì chưa có dữ liệu trogn table

    def __init__(self, id, emoname):
        self.id = id
        self.emoname =emoname

    def __repr__(self):
        return str(self.emoname)


    # Insert value to flask shell:


# ------- End: B3AR config code -------

@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None
