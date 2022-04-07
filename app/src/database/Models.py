from flask_login import UserMixin

from .. import db #this is SQLAlchemy()

class User(db.Model, UserMixin) :
    user_id = db.Column(db.Intiger, primary_key=True)
    username = db.Column(db.String(150))
    full_name = db.Column(db.String(150))
    age = db.Column(db.Intiger)
    email = db.Column(db.String(150))
    phone_number = db.Column(db.String(150))
    bio = db.Column(db.Text)
    privacy_status = db.Column(db.Intiger)
    password = db.Column(db.String(150))

    def __repr__(self):
        return '<User %r>' % self.username

class Message(db.Model) :
    message_id = db.Column(db.Intiger, primary_key=True)
    from_node = db.Column(db.String(150))
    to_node = db.Column(db.String(150))
    title = db.Column(db.String(250))
    content = db.Column(db.Text)

class FriendRequest(db.Model) :
    request_id = db.Column(db.Intiger, primary_key=True)
    from_node = db.Column(db.String(150))
    to_node = db.Column(db.String(150))
    status = db.Column(db.Intiger)


class Vertex(db.Model) :
    vertex_id = db.Column(db.Intiger, primary_key=True)
    from_node = db.Column(db.String(150))
    to_node = db.Column(db.String(150))