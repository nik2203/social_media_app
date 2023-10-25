from flask import Blueprint, render_template
from flask_login import login_required, current_user

from ..database.Models import Friendship, Message

dashboard = Blueprint('dashboard', __name__)
"""
:prefix /dash/<routes>
"""

@dashboard.route('/')
@login_required
def index() :
    """
    main page for user

    login is required

    :context Type[dict]
    :return
        :render dashboard template
    """
    messages = Message.query.filter_by(to_node=current_user.username).all()
    requests = Friendship.query.filter_by(to_node=current_user.username).all()

    context = {
        'messages': messages,
        'requests': requests,
    }

    return render_template('dashboard/index.html', context=context)



@dashboard.route('/friends')
@login_required
def get_friends():
    """
    reads user friends

    login is required

    :context Type[dict]
    :return
        :render dashboard template
    """
    context = {
        'followers': [],
        'followings': [],
    }

    return render_template('dashboard/friends.html', context=context)
