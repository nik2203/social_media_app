from flask import Blueprint

from ..database.Models import User, Friendship, Message

test = Blueprint('test', __name__)

"""

THIS FILE IS JUST FOR TESTING
ITS NOT A PART OF THE APP

"""

@test.route('users')
def get_users():
    res = []
    users = User.query.all()

    for user in users:
        res.append([user.username, user.full_name, user.email])

    return {'res': res}


@test.route('messages')
def get_messages():
    res = []
    messages = Message.query.all()

    for msg in messages:
        res.append([msg.from_node, msg.to_node, msg.content])

    return {'res': res}

@test.route('req')
def get_requests():
    res = []
    reqs = Friendship.query.all()

    for req in reqs:
        res.append([req.from_node, req.to_node, req.status])

    return {'res': res}

