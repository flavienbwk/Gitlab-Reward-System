import uuid
import datetime

from server.create_app import database
from models.badge import Badge


def get_all_badges():
    return Badge.query.all()


def get_a_badge(name):
    return Badge.query.filter_by(name=name).first()


def save_changes(data):
    database.session.add(data)
    database.session.commit()