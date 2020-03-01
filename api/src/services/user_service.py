import uuid
import datetime

from server.create_app import database
from models.user import User


def get_all_users():
    return User.query.all()


def get_a_user(username):
    return User.query.filter_by(username=username).first()


def save_changes(data):
    database.session.add(data)
    database.session.commit()