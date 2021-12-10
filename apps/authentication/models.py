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


# insert value
# https://courses.prettyprinted.com/courses/1016334/lectures/21156810
# https://gist.github.com/crearo/bc23880cf2ba0ec2dc524b66388a0072
# https://pythonbasics.org/flask-sqlalchemy/
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
# https://flask-user.readthedocs.io/en/latest/data_models.html
# https://docs.sqlalchemy.org/en/14/core/type_basics.html
# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many
# https://www.geeksforgeeks.org/connect-flask-to-a-database-with-flask-sqlalchemy/
# https://thaitpham.com/huong-dan-lap-trinh-flask-phan-4-su-dung-co-so-du-lieu/
# https://codepou.com/blog/flask/huong-dan-su-dung-sqlalchemy-trong-ung-dung-flask-framework

# deploy
# https://www.youtube.com/watch?v=i3RMlrx4ol4
# https://www.youtube.com/watch?v=pMIwu5FwJ78
# https://www.youtube.com/watch?v=xl0N7tHiwlw
# https://www.youtube.com/watch?v=qNF1HqBvpGE
# https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/
# https://blog.paperspace.com/deploying-deep-learning-models-flask-web-python/
# https://www.geeksforgeeks.org/deploy-machine-learning-model-using-flask/

# camera
# https://usefulangle.com/post/352/javascript-capture-image-from-camera
# https://usefulangle.com/post/354/javascript-record-video-from-camera
# https://usefulangle.com/post/355/javascript-get-camera-resolution
# https://www.youtube.com/watch?v=vF9QRJwJXJk
# https://blog.miguelgrinberg.com/post/video-streaming-with-flask
# https://www.codegrepper.com/code-examples/python/flask+opening+camera+while+in+1+page+and+closing+on+moving+to+other+page+flask