from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

class User(db.Model, UserMixin) :
    """
    user model

    :primary key: id
    :inherit db.Model, UserMixin
    """
    __tablename__ = 'user'

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    gender = db.Column(db.String(1))
    dateofbirth = db.Column(db.Date)
    bio = db.Column(db.Text)
    

class Message(db.Model) :
    """
    message model

    :primary key: id
    :inherit db.Model
    """
    __tablename__ = 'message'

    messageid = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    timestamps = db.Column(db.Time)
    sender1 = db.Column(db.Integer, db.ForeignKey('user.userid'))
    sender2 = db.Column(db.Integer, db.ForeignKey('user.userid'))

class Friendship(db.Model) :
    """
    friend request model

    :primary key: id
    :inherit db.Model
    """
    __tablename__ = 'friendship'

    FRIENDSHIP_STATUS = ('pending', 'accepted', 'rejected')

    friendshipid = db.Column(db.Integer, primary_key=True)
    userid1 = db.Column(db.Integer, db.ForeignKey('user.userid'))
    userid2 = db.Column(db.Integer, db.ForeignKey('user.userid'))
    status = db.Column(Enum(*FRIENDSHIP_STATUS, name='friendship_status'))

class Post(db.Model) :
    __tablename__ = 'post'

    postid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))
    content = db.Column(db.Text)
    timestamps = db.Column(db.Time)

class Userlike(db.Model) :
    __tablename__ = 'userlike'

    likeid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))
    postid = db.Column(db.Integer, db.ForeignKey('post.postid'))
    timestamps = db.Column(db.Time)

class Comment(db.Model):
    """
    comment model

    :primary key: id
    :inherit db.Model
    """
    __tablename__ = 'comment'

    commentid = db.Column(db.Integer, primary_key=True)
    postid = db.Column(db.Integer, db.ForeignKey('posts.postid'), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), nullable=False)
    content = db.Column(db.Text)
    timestamps = db.Column(db.Time)

class Notification(db.Model):
    """
    notification model

    :primary key: id
    :inherit db.Model
    """
    __tablename__ = 'notification'

    notificationid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), nullable=False)
    content = db.Column(db.Text)
    timestamps = db.Column(db.Time)
